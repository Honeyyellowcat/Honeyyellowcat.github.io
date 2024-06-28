import serial.tools.list_ports  # Package for listing available serial ports
import tkinter as tk  # Importing tkinter and aliasing it as 'tk'
import pyfirmata
import time
import sys

# Define pin numbers
pulPin = 2
dirPin = 3
enPin = 4

# Establish connection to Arduino and configure pins
def connect_to_arduino():
    found_ports = serial.tools.list_ports.comports()
    connect_port = find_arduino(found_ports)
    if connect_port != 'None':
        board = pyfirmata.Arduino(connect_port)
        print('Connected to ' + connect_port)
        board.digital[enPin].write(1)  # Enable motor
        board.digital[dirPin].write(0)  # Set default motor direction
        return board
    else:
        print('Connection Issue!')
        sys.exit()

# Find the Arduino port
def find_arduino(ports_found):
    for port in ports_found:
        if 'COM3' in port.description:  # Adjust for your Arduino's description
            return port.device
    return 'None'

# Step the motor by the given number of steps
def step_motor(steps, board):
    for _ in range(steps):
        board.digital[pulPin].write(1)
        time.sleep(1e-3)
        board.digital[pulPin].write(0)
        time.sleep(1e-3)

# Step motor in the forward direction
def step_forward(board):
    board.digital[dirPin].write(0)  # Set direction forward
    step_motor(100, board)  # Adjust steps as needed

# Step motor in the reverse direction
def step_reverse(board):
    board.digital[dirPin].write(1)  # Set direction reverse
    step_motor(100, board)  # Adjust steps as needed

# GUI
def create_gui():
    root = tk.Tk()
    root.title("Stepper Motor Control")

    step_up_button = tk.Button(root, text="Step Up", command=step_up)
    step_up_button.pack()

    step_down_button = tk.Button(root, text="Step Down", command=step_down)
    step_down_button.pack()

    root.mainloop()

# Button functions
def step_up():
    step_forward(arduino_board)

def step_down():
    step_reverse(arduino_board)

# Connect to Arduino
arduino_board = connect_to_arduino()

# Create GUI
create_gui()
