import tkinter as tk # Importing the tkinter library for GUI
from tkinter import ttk # Importing themed widgets from tkinter for a modern look and feel
import nidaqmx # Importing nidaqmx for interacting with National Instruments Data Acquisition hardware
import numpy as np # Importing numpy for numerical computing
import matplotlib.pyplot as plt # Importing matplotlib.pyplot for plotting and visualization
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Importing FigureCanvasTkAgg from matplotlib.backends.backend_tkagg for embedding matplotlib figures in Tkinter GUIs
import serial # Importing serial for serial communication
import pandas as pd # Importing pandas for data manipulation and analysis


#Can pull up the other graphes 


# Global variables for raw deflection data and uncertainties
deflection_data = []
uncertainties = []

# Global variables for LVDT signal, LVDT displacement range, and velocity change
lvdt_signal_data = []
lvdt_displacement_data = []
velocity_change_data = []

# Function to record raw deflection data from the rangefinder
def record_deflection():
    global deflection_data
    try:
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan("your_channel")
            task.timing.cfg_samp_clk_timing(rate=1000, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS)
            deflection_data = task.read(number_of_samples_per_channel=1000)  # Recording Deflection Data

    except nidaqmx.DaqError as e:
        print(f"DAQ Error: {e}")
        print(f"Error Code: {e.error_code}")
        print(f"Error Details: {e.__cause__}")

# Function to convert deflection measurements to thrust measurements
def convert_to_thrust():
    global deflection_data, uncertainties
    try:
        # Perform Calibration
        calibration_force = 0.01  # Calibrating to 10 micronewtons (0.01 Newtons)
        measured_deflection = 50  # Example measured deflection in units

        # Calculate sensitivity
        sensitivity = measured_deflection / calibration_force

        # Apply calibration to convert deflection measurements to thrust measurements
        thrust_data = deflection_data * sensitivity

        # Set uncertainties to a fixed value
        uncertainties = np.full_like(thrust_data, 0.05)  # Set uncertainties to 0.05 for all measurements

    except Exception as e:
        print(f"An error occurred during conversion: {e}")

# Function to display deflection measurements and corresponding uncertainties graphically
def display_graph():
    global deflection_data, uncertainties
    try:
        # Plot data with uncertainties
        fig = plt.figure(figsize=(8, 6))
        plt.errorbar(np.arange(len(deflection_data)), deflection_data, yerr=uncertainties, fmt='o', ecolor='red',
                     capsize=5)
        plt.xlabel('Time')
        plt.ylabel('Deflection')
        plt.title('Deflection Measurements with Uncertainties')
        plt.grid(True)

        # Save the plot as an image
        fig.savefig('deflection_plot.png')

        # Display the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred during graph display: {e}")

# Function to calculate LVDT displacement range and velocity change
def calculate_lvdt_parameters():
    global lvdt_signal_data, lvdt_displacement_data, velocity_change_data

    # Calculate LVDT displacement range from the LVDT signal
    # Replace the following lines with your actual LVDT signal data processing
    lvdt_displacement_data = np.random.rand(len(lvdt_signal_data)) * 10  # Example LVDT displacement data
    # Calculate velocity change from LVDT displacement data
    velocity_change_data = np.diff(lvdt_displacement_data)

# Function to plot LVDT signal vs. time
def plot_lvdt_signal():
    global lvdt_signal_data
    try:
        # Plot LVDT signal vs. time
        plt.figure(figsize=(8, 6))
        plt.plot(np.arange(len(lvdt_signal_data)), lvdt_signal_data, color='blue')
        plt.xlabel('Time')
        plt.ylabel('LVDT Signal (V)')
        plt.title('LVDT Signal vs. Time')
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"An error occurred during LVDT signal plot: {e}")

# Function to plot LVDT displacement range vs. impulse
def plot_lvdt_displacement():
    global lvdt_displacement_data
    try:
        # Plot LVDT displacement range vs. impulse
        plt.figure(figsize=(8, 6))
        plt.plot(lvdt_displacement_data, color='green')
        plt.xlabel('Impulse (N-s)')
        plt.ylabel('LVDT Displacement Range (V)')
        plt.title('LVDT Displacement Range vs. Impulse')
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"An error occurred during LVDT displacement plot: {e}")

# Function to plot velocity change vs. calibration impulse
def plot_velocity_change():
    global velocity_change_data
    try:
        # Plot velocity change vs. calibration impulse
        plt.figure(figsize=(8, 6))
        plt.plot(velocity_change_data, color='red')
        plt.xlabel('Calibration Impulse (\u03BCNs)')
        plt.ylabel('Velocity Change (V/s)')
        plt.title('Velocity Change vs. Calibration Impulse')
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"An error occurred during velocity change plot: {e}")

# Function to export figures and raw data
def export_data():
    global deflection_data, uncertainties
    try:
        # Save raw data to a CSV file
        df = pd.DataFrame({'Deflection': deflection_data, 'Uncertainties': uncertainties})
        df.to_csv('C:/Users/every/OneDrive/Desktop/CODE/PPT/raw_data.csv', index=False)

        print("Raw data exported successfully.")

    except Exception as e:
        print(f"An error occurred during data export: {e}")

# Create main window
root = tk.Tk()
root.title("Deflection Data Analysis")

# Create frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=5)

# Create buttons for recording, converting, and displaying data
record_button = ttk.Button(button_frame, text="Record Deflection", command=record_deflection)
record_button.grid(row=0, column=0, padx=5)

convert_button = ttk.Button(button_frame, text="Convert to Thrust", command=convert_to_thrust)
convert_button.grid(row=0, column=1, padx=5)

plot_button = ttk.Button(button_frame, text="Display Graph", command=display_graph)
plot_button.grid(row=0, column=2, padx=5)

export_button = ttk.Button(button_frame, text="Export Data", command=export_data)
export_button.grid(row=0, column=3, padx=5)

# Create buttons for additional plots
lvdt_signal_button = ttk.Button(button_frame, text="Plot LVDT Signal", command=plot_lvdt_signal)
lvdt_signal_button.grid(row=1, column=0, padx=5)

lvdt_displacement_button = ttk.Button(button_frame, text="Plot LVDT Displacement", command=plot_lvdt_displacement)
lvdt_displacement_button.grid(row=1, column=1, padx=5)

velocity_change_button = ttk.Button(button_frame, text="Plot Velocity Change", command=plot_velocity_change)
velocity_change_button.grid(row=1, column=2, padx=5)

# Create quit button
quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=5)

root.mainloop()
