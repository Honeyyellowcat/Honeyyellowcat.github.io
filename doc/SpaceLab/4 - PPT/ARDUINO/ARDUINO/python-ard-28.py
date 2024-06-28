
# https://www.youtube.com/watch?v=idVcItHfGS4
# https://mytectutor.com/how-to-control-stepper-motor-using-l298n-motor-driver-and-arduino/

import serial  # Package for serial communication
import serial.tools.list_ports  # Package for listing available serial ports
from tkinter import *  # Importing all modules from tkinter
import tkinter as tk  # Importing tkinter and aliasing it as 'tk'

# Defining the variables
motRun = "1" # Motor activation flag
indexA =  "A" # Data start marker
indexD =  "D" # Direction marker 
newLine = "\n" # New line marker

# Here we are defining the serial port and opening up before sending any data
serialInst = None
portVal = "/dev/cu.usbmodem11101" # Change this to match the port where your Arduino is connected

try:
    import serial
    serialInst = serial.Serial(portVal, 9600) #Ensure that the baud rate (9600 in this case) matches the baud rate specified in the Arduino code (Serial.begin(9600)).
    print(f"Serial port {portVal} opened successfully.")
except serial.SerialException as e:
    print(f"Failed to open serial port {portVal}: {e}")

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
    canvas.itemconfig(confirm_text, text = "Data Sent")
    root.after(1000, confirmTransferReset)

# Resetting the confirmation message 
def confirmTransferReset():
    canvas.itemconfig(confirm_text, text = "")

# Function to quit the application
def quitApplication():
    root.destroy()

# Functions to enable clockwise and anticlockwise rotation and to initiate the transmission of data to serial
def RotateClockwise():
    motDir = "Clockwise"
    sendData(motDir)
def RotateAnticlockwise():
    motDir = "Anticlockwise"
    sendData(motDir)

# GUI configuration
root = Tk()
root.title("Arduino Controller")

# GUI layout
# Set the width and height of the canvas
canvas_width = 600
canvas_height = 450

# creating the image for the GUI

motor_img = PhotoImage(file=r"C:\Users\every\OneDrive\Desktop\CODE\PPT\MASTER\Arduino_and_python\StepperMotor_ROHS.png")
canvas = Canvas(width=canvas_width, height=canvas_height)  # Adjust width and height as needed
canvas.create_image(canvas_width/2, canvas_height/2, image=motor_img)  # Center the image
canvas.grid(row=0, column=0, columnspan=2, padx=20, pady=20)  # Adding padding around the canvas
confirm_text = canvas.create_text(canvas_width/2, canvas_height/2, text="", fill="red", font=("Courier", 20, "bold"))  # Center the text

# Creating the buttons to set the direction of the rotation and to transmit data to the serial
btn_forward = tk.Button(root, text="Step down", command=RotateClockwise)
btn_forward.grid(row=1, column=0, padx=10, pady=10)  # Adding padding around the button

btn_backward = tk.Button(root, text="Step up", command=RotateAnticlockwise)
btn_backward.grid(row=1, column=1, padx=10, pady=10)  # Adding padding around the button

# Adding a quit button
btn_quit = tk.Button(root, text="Quit", command=quitApplication)
btn_quit.grid(row=2, column=0, columnspan=2, pady=0)  # Adding padding below the buttons

# Defining the size of the window and looping through to maintain the interface
root.geometry(f"{canvas_width}x{canvas_height + 200}")  # Adjust height to accommodate buttons and labels
root.mainloop()
