import tkinter as tk # Importing the tkinter library for GUI DAQ_Python.py
from tkinter import ttk # Importing themed widgets from tkinter for a modern look and feel
import nidaqmx # Importing nidaqmx for interacting with National Instruments Data Acquisition hardware
import numpy as np # Importing numpy for numerical computing
import matplotlib.pyplot as plt # Importing matplotlib.pyplot for plotting and visualization
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Importing FigureCanvasTkAgg from matplotlib.backends.backend_tkagg for embedding matplotlib figures in Tkinter GUIs
import serial # Importing serial for serial communication
import pandas as pd # Importing pandas for data manipulation and analysis
from scipy.signal import butter, lfilter # pass filter

# pip install pyarrow

# 1. Known Impulse from combs: given by grad 


# Plots will be 2 and a third additional 

# QUESTIONS ------------------------
# 1. To clarify for the linear impulse plot. i understand i am given approximatly 3 impulse bit values.  
    # with that i understand there will be one V_{max} value assosiated with one impuse bit value. does this mean i will have to run 
    # the thruster 3 different times for 3 different impulse values to collect the data and then continue to calculate out c. 
# 3. As for the delta_x vs time  plot just to clarify. what would b_lazer be? is it Measurement range (75 to 130 mm 2.95" to 5.12") in the calibration manual 
    # https://www.keyence.com/products/sensor/positioning/il/models/il-100/
# 1. Is Sensitivity 
    # sensitivity = (Change in linear velocity due to impulse) / (Impulse bit)
    # So for us it would be caculated c that we calculated from the vmax vs impulse over plot over the Impulse. 
    # and this represents the sensitivity of the laser sensor correct? 
    # justin paper "The sensitivity derived from the calibration data is a first order effect on the accuracy of the final measurement."
# 2. For calculating the uncertaintly. i understand that the standard deviation isnt the 
    # correct approach acordingly to PDR discutions so would i simplely use a normal uncertainty comand on python after the lowpass filter has been applied?

#ttl triger
#send out a 5 volt to times things

# Software will convert deflection measurements to thrust measurements and corresponding uncertainties.
# Software will record raw deflection data from the rangefinder.
# Software will display deflection measurements and corresponding uncertainties graphically, allowing for the export of produced figures and raw data.

# new questions
# 1. thrust measurments no 
# 2 uncertainties 5 - 10 to be able to pull it out 

# 3. sensitivity? amount of defection per unit thrust

# 1. how would the arduino sence that the stepper motor needs adjustment. where is the live data from the arduino coming from. 
# 2. dose the lever really move up and dow +/- 3
# 3. do i need to generate any other plots 

# Global variables for raw deflection data and uncertainties
deflection_data = []
uncertainties = []
# Define known impulses and their corresponding V_max values
known_impulses = [1, 2, 3]  # Insert known impulses
v_max_values = []  # Store the V_max values obtained from find_peak()

# 1)  Function to record raw deflection data from the rangefinder
def record_deflection():
    global deflection_data  # Declaring a global variable to store the deflection data
    try:
        # Create a task for data acquisition
        with nidaqmx.Task() as task:  # Establishing a task for NI-DAQmx operations
            # Add an analog input voltage channel (replace "your_channel" with the actual channel name)
            task.ai_channels.add_ai_voltage_chan("your_channel")  # Configuring an analog input channel for voltage readings
            # Configure the timing for data acquisition
            task.timing.cfg_samp_clk_timing(rate=1000, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS)  # Configuring the sampling clock timing
            # Read raw deflection data from the DAQ device
            deflection_data = task.read(number_of_samples_per_channel=1000)  # Reading raw data from the DAQ device
    # Handle any DAQ errors that may occur
    except nidaqmx.DaqError as e:
        # Print the DAQ error message
        print(f"DAQ Error: {e}")
        # Print the error code associated with the DAQ error
        print(f"Error Code: {e.error_code}")
        # Print any additional error details
        print(f"Error Details: {e.__cause__}")

# 2) have code identify the v_0 becayse voltage wont automaticly start at 0

# 3) Function to find the peak value
    # This function aims to determine the peak value of the given deflection_data array. 
    # The peak value is crucial for calibrating a linear impulse plot to find 'c'.def find_peak():
def find_peak():
    global deflection_data
    if deflection_data:
        try:
            data_array = np.array(deflection_data)
            if data_array.size > 0:
                peak_value = np.max(data_array)
                return peak_value
            else:
                print("Empty array. No peak value found.")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    else:
        print("No deflection data available. Please record deflection data first.")
        return None

def plot_peak():
    global deflection_data
    peak_value = find_peak()
    if peak_value is not None:
        plt.plot(deflection_data, label='Deflection Data')
        plt.plot(np.argmax(deflection_data), peak_value, 'ro', label=f'Peak Value: {peak_value}')
        plt.xlabel('Time')
        plt.ylabel('Deflection')
        plt.title('Deflection Data with Peak Value')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Unable to plot. No peak value found.")

# 4) Function to calculate the calibration constant c using linear regression
# The calibration constant c is calculated as the ratio of V_max to the number of impulses (c = V/N)
def calculate_c():
    global known_impulses, v_max_values
    # Checking if the number of recorded known impulses matches the number of recorded V_max values
    if len(known_impulses) != len(v_max_values):
        print("Please ensure you have recorded all V_max values for known impulses.")
        return
    # Plotting V_max vs known impulses
    plt.figure(figsize=(8, 6))
    plt.scatter(known_impulses, v_max_values, color='blue', label='Data Points')
    plt.xlabel('Known Impulses')
    plt.ylabel('V_max')
    plt.title('V_max vs Known Impulses')
    plt.grid(True)

    # Performing linear regression to find the slope (c)
    slope, intercept = np.polyfit(known_impulses, v_max_values, 1)
    # Plotting the linear regression line
    x_values = np.array(known_impulses)
    y_values = slope * x_values + intercept
    plt.plot(x_values, y_values, color='red', label='Linear Regression')
    # Printing the slope (c), which represents the calibration constant
    print("Slope (c):", slope)
    # Adding legend
    plt.legend()
    # Displaying the plot
    plt.show()

# 5) Function to apply low-pass filter
def apply_lowpass_filter(data):
    # Define filter parameters
    fs = 1000  # Sampling frequency
    cutoff_frequency = 50  # Cutoff frequency in Hz
    # Normalize the cutoff frequency
    nyquist_frequency = 0.5 * fs
    normal_cutoff = cutoff_frequency / nyquist_frequency
    # Define filter order and get filter coefficients
    order = 5
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    # Apply filter to data
    filtered_data = lfilter(b, a, data)
    return filtered_data

# 6) Uncertainty
def c_and_I_uncertainty(force, time):
    try:
        # Constants
        constant_uncertainty = 0.1  # Adjust this value based on your specific case
        # Calculate uncertainty for force and time
        force_uncertainty = constant_uncertainty * force
        time_uncertainty = constant_uncertainty * time
        # Propagation of uncertainty for impulse
        impulse = force * time
        impulse_uncertainty = math.sqrt((force_uncertainty * time)**2 + (time_uncertainty * force)**2)
    except Exception as e:
        print(f"An error occurred during Uncertainty: {e}")
    
# 7) Function to display graph
def display_graph():
    global deflection_data, c_and_I_uncertainty
    try:
        # Apply low-pass filter to smoothen noise
        deflection_data_filtered = apply_lowpass_filter(deflection_data)
        # Plot filtered data
        fig = plt.figure(figsize=(8, 6))
        plt.plot(deflection_data_filtered)
        plt.xlabel('Time')
        plt.ylabel('Voltage')
        plt.title('Thruster Impulse')
        plt.grid(True)
        # Display the plot
        plt.show()
    except Exception as e:
        print(f"An error occurred during graph display: {e}")

# Function to export figures and raw data
def export_data():
    global deflection_data, uncertainties
    try:
        # Save raw data to a CSV file
        df = pd.DataFrame({'Deflection': deflection_data})
        df.to_csv('raw_data.csv', index=False)
        print("Raw data exported successfully.")
    except Exception as e:
        print(f"An error occurred during data export: {e}")

def plot_v_max():
    global known_impulses, v_max_values
    if len(known_impulses) != len(v_max_values):
        print("Please ensure you have recorded all V_max values for known impulses.")
        return
    # Plot V_max vs known impulses
    plt.figure(figsize=(8, 6))
    plt.scatter(known_impulses, v_max_values, color='blue', label='Data Points')
    plt.xlabel('Known Impulses')
    plt.ylabel('V_max')
    plt.title('V_max vs Known Impulses')
    plt.grid(True)

    # Perform linear regression
    slope, intercept = np.polyfit(known_impulses, v_max_values, 1)
    # Plot the linear regression line
    x_values = np.array(known_impulses)
    y_values = slope * x_values + intercept
    plt.plot(x_values, y_values, color='red', label='Linear Regression')
    # Print the slope (c)
    print("Slope (c):", slope)
    # Add legend
    plt.legend()
    # Show plot
    plt.show()

# Create main window
root = tk.Tk()
root.title("Deflection Data Analysis")

# Create frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=5)

# Test Section Header
test_header_label = ttk.Label(button_frame, text="Calibration ", font=('Arial', 12, 'bold'))
test_header_label.grid(row=0, columnspan=2, pady=5)

# Create buttons for recording, converting, and displaying data
record_button = ttk.Button(button_frame, text="Record Raw Deflection", command=record_deflection)
record_button.grid(row=1, column=0, padx=5)

peak_button = ttk.Button(button_frame, text="Calculate Constant C", command=find_peak)
peak_button.grid(row=1, column=1, padx=5)

calculate_button = ttk.Button(button_frame, text="Plot: Vₘₐₓ Peak", command=calculate_c)
calculate_button.grid(row=2, column=0, padx=5)

# Plot V_max vs Known Impulses button
plot_v_max_button = ttk.Button(button_frame, text="Plot: Linear Impulse", command=plot_v_max)
plot_v_max_button.grid(row=2, column=1, padx=5)

# Add separator line
separator = ttk.Separator(button_frame, orient='horizontal')
separator.grid(row=3, columnspan=2, sticky='ew', pady=5)

# Calibration Section Header
calibration_header_label = ttk.Label(button_frame, text="Testing", font=('Arial', 12, 'bold'))
calibration_header_label.grid(row=4, columnspan=2, pady=5)

# Display Graph button
display_graph_button = ttk.Button(button_frame, text="Test", command=display_graph)
display_graph_button.grid(row=5, column=0, padx=5)

# Display Graph button
display_graph_button = ttk.Button(button_frame, text="Plot: Thruster Impulse", command=display_graph)
display_graph_button.grid(row=5, column=1, padx=5)

# Export Data button
export_button = ttk.Button(button_frame, text="Export Data and Plots", command=export_data)
export_button.grid(row=6, column=1, padx=5)

# Create quit button
quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=5)

root.mainloop()
