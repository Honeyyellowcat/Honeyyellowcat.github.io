import serial  # Package for serial communication
from tkinter import *  # Importing all modules from tkinter
import tkinter as tk  # Importing tkinter and aliasing it as 'tk'
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random  # Import the random module TAKE OUT AFTER DEMO

# Defining the variables
motRun = "1"  # Motor activation flag
indexA = "A"  # Data start marker
indexD = "D"  # Direction marker
newLine = "\n"  # New line marker

# Define variables for low-pass filter
alpha = 0.1
filtered_speed = 0

# Here we are defining the serial port and opening up before sending any data
serialInst = None
portVal = "/dev/cu.usbmodem11101"

try:
    import serial
    serialInst = serial.Serial(portVal, 9600)
    print(f"Serial port {portVal} opened successfully.")
except serial.SerialException as e:
    print(f"Failed to open serial port {portVal}: {e}")

# Function to quit the application
def quitApp():
    if serialInst:
        serialInst.close()  # Close the serial port before quitting
    root.quit()

# Sending the data to Serial Port
def sendData(motDir):
    if serialInst:
        serialInst.write(motRun.encode('utf-8'))
        serialInst.write(indexA.encode('utf-8'))
        serialInst.write(motDir.encode('utf-8'))
        serialInst.write(indexD.encode('utf-8'))
        serialInst.write(newLine.encode('utf-8'))
        confirmTransfer()
        print("Data Sent")
    else:
        print("Serial port not available.")

# Showing confirmation message that the data has been sent in GUI
def confirmTransfer():
    canvas.itemconfig(confirm_text, text="Data Sent")
    root.after(1000, confirmTransferReset)

# Resetting the confirmation message
def confirmTransferReset():
    canvas.itemconfig(confirm_text, text="")

# Functions to enable clockwise and anticlockwise rotation and to initiate the transmission of data to serial
def RotateClockwise():
    motDir = "Clockwise"
    sendData(motDir)

def RotateAnticlockwise():
    motDir = "Anticlockwise"
    sendData(motDir)

# Function to update the plot data
def update_plot(frame):
    # Here you will update the plot data based on the data received from the Arduino or any other source
    # For now, let's just show a dummy sine wave
    x_data.append(frame)
    y_data.append((frame % 100) - 50)  # A dummy sine wave for demonstration
    line.set_data(x_data, y_data)
    return line,

# GUI configuration
root = Tk()
root.title("Arduino Controller")

# GUI layout
# Set the width and height of the canvas
canvas_width = 600
canvas_height = 200

canvas = Canvas(width=canvas_width, height=canvas_height)  # Adjust width and height as needed
canvas.grid(row=0, column=0, columnspan=2)
confirm_text = canvas.create_text(canvas_width / 2, canvas_height / 2, text="", fill="red",
                                  font=("Courier", 20, "bold"))  # Center the text

# Initialize a variable to keep track of the current displacement
current_displacement = 0

# Function to update the plot data
def update_plot(frame):
    global current_displacement
    
    # Define the fixed displacement increment
    displacement_increment = 0.1  # Adjust as needed
    
    # Update the current displacement by adding the fixed increment
    current_displacement += displacement_increment
    
    # Append the current time and displacement to the data lists
    x_data.append(x_data[-1] + 1)  # Increment x-axis by 1 at each frame
    y_data.append(current_displacement)
    
    # Update the plot
    line.set_data(x_data[-100:], y_data[-100:])  # Show only the last 100 data points
    
    return line,


#Function to update the plot data
def update_plot(frame):
    global current_displacement
    
    #Generate a random displacement value
    displacement = random.uniform(-1, 1)  # Adjust the range as needed
    
    #Update the current displacement by adding the new displacement value
    current_displacement += displacement
    
   # Ensure the displacement never goes below 0
    current_displacement = max(0, current_displacement)
    
   # Append the current time and displacement to the data lists
    x_data.append(frame)
    y_data.append(current_displacement)
    
  #  Update the plot
    line.set_data(x_data, y_data)
    return line,

# Creating the live feed plot
fig, ax = plt.subplots(figsize=(6, 4))  # Adjust the second value (height) as needed
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 100)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Stepper Motor Calibration')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')

# Adding a horizontal line at y=0
ax.axhline(0, color='black', linestyle='--')  # Adjust color and linestyle as needed

# Initialize plot data
x_data, y_data = [], []

# Integrate the plot into Tkinter GUI
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=0, columnspan=2)

# Creating the buttons to set the direction of the rotation and to transmit data to the serial
btn_forward = tk.Button(root, text="Clockwise", command=RotateClockwise)
btn_forward.grid(row=2, column=0)

btn_backward = tk.Button(root, text="Anticlockwise", command=RotateAnticlockwise)
btn_backward.grid(row=2, column=1)

# Creating the quit button
btn_quit = tk.Button(root, text="Quit", command=quitApp)
btn_quit.grid(row=3, column=0, columnspan=2)

# Start the animation to update the plot
ani = FuncAnimation(fig, update_plot, frames=range(100), interval=100)

# Defining the size of the window and looping through to maintain the interface
root.geometry(f"{canvas_width}x{canvas_height + 250}")  # Adjust height to accommodate buttons and labels
root.mainloop()
