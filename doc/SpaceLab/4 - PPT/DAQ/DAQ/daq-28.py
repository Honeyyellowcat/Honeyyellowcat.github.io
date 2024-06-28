import tkinter as tk  # Import the tkinter module for creating GUI
from tkinter import ttk  # Import themed widgets from tkinter for a modern look and feel
import nidaqmx  # Import nidaqmx for interacting with National Instruments Data Acquisition hardware
import numpy as np  # Import numpy for numerical computing
import matplotlib.pyplot as plt  # Import matplotlib.pyplot for plotting and visualization
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Import FigureCanvasTkAgg from matplotlib.backends.backend_tkagg for embedding matplotlib figures in Tkinter GUIs
import pandas as pd  # Import pandas for data manipulation and analysis
from scipy.signal import butter, lfilter  # Import butter and lfilter from scipy.signal for low-pass filter
import time  # Import the time module for timestamping

# Global variables for raw deflection data and uncertainties
deflection_data = []  # Initialize an empty list to store raw deflection data
vpeak_values = []  # Initialize an empty list to store V_peak values
test_counter = 0  # Counter to keep track of the number of tests conducted

# Known impulses and their corresponding V_max values
known_impulses = [1, 2, 3]  # Define known impulses
calibration_constant = None  # Initialize calibration constant

# Function to trigger TTL signal
def trigger_ttl():
    try:
        # task for digital output
        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan('Dev1/ai0')  # Set the digital output channel
            task.write(True)  # TTL high signal
            time.sleep(0.1)   # for 0.1 second
            task.write(False) # TTL low signal
    except nidaqmx.DaqError as e:
        print(f"TTL Triggering Error: {e}")

# Function to record raw deflection data from the rangefinder
def record_deflection():
    global deflection_data, vpeak_values
    trigger_ttl()
    
    try:
        # Create a task for data acquisition ( try to use the return function istead of the global data)
        with nidaqmx.Task() as task:
            # Automatically detect and use the first available device
            task.ai_channels.add_ai_voltage_chan("Dev1/ai0", terminal_config=nidaqmx.constants.TerminalConfiguration.DEFAULT)
            task.read()

            # Timing for data acquisition
            task.timing.cfg_samp_clk_timing(rate=10000, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS)
            
            # Read raw deflection data from DAQ for 30 seconds
            start_time = time.time()  # Record the start time
            deflection_data = task.read(number_of_samples_per_channel=1000)  # Read raw data from DAQ
            end_time = time.time()  # Record the end time
            elapsed_time = end_time - start_time  # Calculate the elapsed time
            
            # Calculate the actual sampling rate
            actual_sampling_rate = len(deflection_data[0]) / elapsed_time  # Calculate sampling rate
            print(f"Actual Sampling Rate: {actual_sampling_rate} samples per second")  # Print the actual sampling rate
            
            # Check if the actual sampling rate matches the expected rate
            if actual_sampling_rate != 10000:  # Check if actual sampling rate matches expected rate
                print("Warning: Actual sampling rate does not match the expected rate.")
            
            # Apply low-pass filter to smoothen noise
            fs = 10000  # Define sampling frequency
            cutoff_frequency = 50  # Define cutoff frequency in Hz
            nyquist_frequency = 0.5 * fs  # Calculate Nyquist frequency
            normal_cutoff = cutoff_frequency / nyquist_frequency  # Normalize cutoff frequency
            order = 5  # Define filter order
            b, a = butter(order, normal_cutoff, btype='low', analog=False)  # Compute filter coefficients
            filtered_data = lfilter(b, a, deflection_data[0])  # Apply filter to data
            
            # Find the peak value in the filtered data
            peak_value = np.max(filtered_data)  # Find maximum value in filtered data
            
            # Store the peak value
            vpeak_values.append(peak_value)  # Append peak value to vpeak_values list
            
            # Check if we have reached three peak values for each known impulse
            if len(vpeak_values) == len(known_impulses) * 3:  # Check if we have enough peak values
                print("Three V_peak values reached for each known impulse.")
                calculate_calibration_constant()  # Calculate calibration constant
                plot_calibration()  # Plot calibration curve
            
    except nidaqmx.DaqError as e:  # Handle DAQ errors
        print(f"DAQ Error: {e}")
        print(f"Error Code: {e.error_code}")
        print(f"Error Details: {e.__cause__}")

# Function to calculate calibration constant
def calculate_calibration_constant():
    global calibration_constant, vpeak_values, known_impulses
    
    # Check if the length of vpeak_values is sufficient
    if len(vpeak_values) < len(known_impulses) * 3:
        print("Not enough peak values recorded for calibration.")
        return
    
    calibration_constants = []
    
    # Iterate over each known impulse
    for i in range(len(known_impulses)):
        # Iterate over each of the three peak values recorded for the current impulse
        for j in range(3):
            # Calculate the index to access the peak value in vpeak_values
            index = i * 3 + j
            # Check if the index is within the range of vpeak_values
            if index < len(vpeak_values):
                # Calculate the calibration constant for the current peak value and impulse
                calibration_constants.append(vpeak_values[index] / known_impulses[i])
            else:
                print(f"Error: Index {index} out of range for vpeak_values.")
                return
    
    # Compute the mean of all calibration constants to obtain the final calibration constant
    calibration_constant = np.mean(calibration_constants)

    # Print the calculated calibration constant
    print("Calibration Constant (c):", calibration_constant)

# Function to plot calibration curve
def plot_calibration():
    global known_impulses, vpeak_values, calibration_constant
    
    # Plot calibration curve
    plt.figure(figsize=(8, 6))
    plt.scatter(known_impulses, [vpeak_values[i] / known_impulses[i] for i in range(len(known_impulses))], color='blue', label='Data Points')
    plt.xlabel('Known Impulses')
    plt.ylabel('V_peak / N')
    plt.title('Calibration Curve')
    plt.grid(True)

    # Add linear regression line
    slope, _ = np.polyfit(known_impulses, [vpeak_values[i] / known_impulses[i] for i in range(len(known_impulses))], 1)
    plt.plot(known_impulses, [slope * impulse for impulse in known_impulses], color='red', label='Linear Regression')
    plt.legend()
    plt.show()

# Function to conduct a test
def conduct_test():
    global test_counter, calibration_constant
    trigger_ttl()
    
    # Increment the test counter
    test_counter += 1
    
    try:
        # Create a task for data acquisition
        with nidaqmx.Task() as task:
            # Automatically detect and use the first available device
            task.ai_channels.add_ai_voltage_chan("Dev1/ai0", terminal_config=nidaqmx.constants.TerminalConfiguration.DEFAULT)
            task.read()

            # Timing for data acquisition
            task.timing.cfg_samp_clk_timing(rate=10000, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS)
            
            # Read raw deflection data from DAQ for 30 seconds
            start_time = time.time()
            deflection_data = task.read(number_of_samples_per_channel=1000)
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            # Calculate the actual sampling rate
            actual_sampling_rate = len(deflection_data[0]) / elapsed_time
            
            # Print the actual sampling rate
            print(f"Actual Sampling Rate: {actual_sampling_rate} samples per second")
            
            # Check if the actual sampling rate matches the expected rate
            if actual_sampling_rate != 10000:  
                print("Warning: Actual sampling rate does not match the expected rate.")
            
            # Apply low-pass filter to smoothen noise
            fs = 10000  # Sampling frequency
            cutoff_frequency = 50  # Cutoff frequency in Hz
            nyquist_frequency = 0.5 * fs
            normal_cutoff = cutoff_frequency / nyquist_frequency
            order = 5
            b, a = butter(order, normal_cutoff, btype='low', analog=False)
            filtered_data = lfilter(b, a, deflection_data[0])
            
            # Save test data to a CSV file
            df = pd.DataFrame({'Deflection': filtered_data})
            # Insert calibration constant (c) at the top of the CSV table
            df.insert(0, 'Calibration Constant (c)', calibration_constant)
            df.to_csv(f'test_data_{test_counter}.csv', index=False)
            print(f"Test {test_counter} data exported successfully.")
            
    except nidaqmx.DaqError as e:
        print(f"DAQ Error: {e}")
        print(f"Error Code: {e.error_code}")
        print(f"Error Details: {e.__cause__}")

# Function to plot the thruster impulse after conducting the test
def plot_thruster_impulse():
    global test_counter
    
    # Load test data from the CSV file of the latest test
    try:
        df = pd.read_csv(f'test_data_{test_counter}.csv')
    except FileNotFoundError:
        print("Error: Test data file not found.")
        return
    
    # Plot the thruster impulse
    plt.figure(figsize=(8, 6))
    plt.plot(df['Deflection'], label=f'Test {test_counter} Thruster Impulse')
    plt.xlabel('Time')
    plt.ylabel('Deflection')
    plt.title('Thruster Impulse Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to export raw deflection data to CSV file
def export_raw_data():
    global deflection_data
    
    try:
        # Save raw data to a CSV file
        df = pd.DataFrame({'Deflection': deflection_data[0]})
        df.to_csv('raw_data.csv', index=False)
        print("Raw deflection data exported successfully.")
    except Exception as e:
        print(f"An error occurred during data export: {e}")

# Function to export test data to CSV file
def export_test_data():
    global test_counter
    
    try:
        # Load test data from the CSV file of the latest test
        df = pd.read_csv(f'test_data_{test_counter}.csv')
        df.to_csv(f'test_data_export_{test_counter}.csv', index=False)
        print(f"Test {test_counter} data exported successfully.")
    except FileNotFoundError:
        print("Error: Test data file not found.")
    except Exception as e:
        print(f"An error occurred during data export: {e}")

# Create main window
root = tk.Tk()
root.title("Deflection Data Analysis")

# Create frame for calibration section
calibration_frame = ttk.Frame(root, padding="20")
calibration_frame.pack(fill="both", expand=True, padx=5, pady=5)

# Calibration Section Header
calibration_header_label = ttk.Label(calibration_frame, text="Calibration", font=('Arial', 12, 'bold'))
calibration_header_label.grid(row=0, column=0, columnspan=2, pady=5)

# Create button for recording data
record_button = ttk.Button(calibration_frame, text="Record Raw Deflection", command=record_deflection)
record_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Create button for calculating calibration constant
calibrate_button = ttk.Button(calibration_frame, text="Calibrate C", command=calculate_calibration_constant)
calibrate_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Plot V_max vs Known Impulses button
plot_vpeak_button = ttk.Button(calibration_frame, text="Plot Linear Impulse", command=plot_calibration)
plot_vpeak_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Create button for exporting raw deflection data
export_raw_button = ttk.Button(calibration_frame, text="Export Raw Deflection Data", command=export_raw_data)
export_raw_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Add separator line
separator = ttk.Separator(calibration_frame, orient='horizontal')
separator.grid(row=4, column=0, columnspan=2, sticky='ew', pady=10)

# Create frame for testing section
testing_frame = ttk.Frame(root, padding="10")
testing_frame.pack(fill="both", expand=True, padx=5, pady=5)

# Testing Section Header
testing_header_label = ttk.Label(testing_frame, text="Testing", font=('Arial', 12, 'bold'))
testing_header_label.grid(row=0, column=0, columnspan=2, pady=5)

# Create button for conducting a test
test_button = ttk.Button(testing_frame, text="Conduct Test", command=conduct_test)
test_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Create button for plotting the thruster impulse
plot_button = ttk.Button(testing_frame, text="Plot Thruster Impulse", command=plot_thruster_impulse)
plot_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Create button for exporting test data
export_test_button = ttk.Button(testing_frame, text="Export Test Data", command=export_test_data)
export_test_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Create quit button
quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

root.mainloop()