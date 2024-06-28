import serial  # Package for serial communication
import serial.tools.list_ports  # Package for listing available serial ports
import pyfirmata
import time
import sys 
from tkinter import *  # Importing all modules from tkinter
import tkinter as tk  # Importing tkinter and aliasing it as 'tk'


#Important! For code to function properly, make sure motor driver + ports are plugged into Arduino 5V
#and motor driver - ports are plugged into Arduino digital pins defined below

#Define pin numbers
pulPin=2
dirPin=3
enPin=4

def get_ports(): #port
    ports=serial.tools.list_ports.comports()
    return ports

def findArduino(portsFound): #finding the arduino ports 
    commPort='None'
    numConnection=len(portsFound)
    for i in range(0,numConnection):
        port=portsFound[i]
        #print(port)
        strPort=str(port)
        if 'HostDevice' in strPort:
            splitPort=strPort.split(' ')
            commPort=(splitPort[0])
    return commPort

def stepX(steps): #defining the step function
    for i in range(0,steps):
        board.digital[pulPin].write(1)
        time.sleep(1e-3)
        board.digital[pulPin].write(0)
        time.sleep(1e-3)


foundPorts=get_ports()
connectPort=findArduino(foundPorts)

if connectPort != 'None':
    #ser=serial.Serial(connectPort, baudrate=9600, timeout=1)
    board=pyfirmata.Arduino(connectPort)
    print('Connected to '+connectPort)
else:
    print('Connection Issue!')
    sys.exit()

board.digital[enPin].write(1) #enable motor
board.digital[dirPin].write(0) #set motor direction. 1 is , 0 is 

# here
def RotateClockwise():
    stepX(1000)
    board.digital[dirPin].write(0) 

def RotateAnticlockwise(): 
    board.digital[dirPin].write(1)  
    stepX(1000) 
# stepX(1000)

#GUI Layout 
root = Tk()
root.title("Arduino Controller")

# Direction of the rotation and to transmit data to the serial
btn_forward = tk.Button(root, text="Step down", command=RotateClockwise)
btn_forward.grid(row=1, column=0, padx=10, pady=10)  # Adding padding around the button

btn_backward = tk.Button(root, text="Step up", command=RotateAnticlockwise)
btn_backward.grid(row=1, column=1, padx=10, pady=10)  # Adding padding around the button

# Quit button
def quitApplication(): # Function to quit the application
    root.destroy()
btn_quit = tk.Button(root, text="Quit", command=quitApplication)
btn_quit.grid(row=2, column=0, columnspan=2, pady=0)  # Adding padding below the buttons

# Defining the size of the window and looping through to maintain the interface
canvas_width = 600 # Set the width and height of the canvas
canvas_height = 450
root.geometry(f"{canvas_width}x{canvas_height + 200}")  # Adjust height to accommodate buttons and labels
root.mainloop()