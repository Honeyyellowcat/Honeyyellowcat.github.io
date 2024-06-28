import tkinter as tk
import serial

def move_stepper(steps):
    ser.write(str(steps).encode())  # Send steps to Arduino
    print(ser.readline().decode())  # Receive acknowledgment from Arduino

def clockwise():
    move_stepper(200)

def counterclockwise():
    move_stepper(-200)

def stop():
    move_stepper(0)  # Send 0 steps to stop the motor

# Create Tkinter window
root = tk.Tk()
root.title("Stepper Control")

# Create buttons for clockwise and counterclockwise movement
clockwise_button = tk.Button(root, text="Clockwise", command=clockwise)
clockwise_button.pack()

counterclockwise_button = tk.Button(root, text="Counterclockwise", command=counterclockwise)
counterclockwise_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack()

# Initialize serial communication with Arduino
ser = serial.Serial('COM3', 9600)  # Replace 'COMX' with your Arduino's COM port

# Start Tkinter event loop
root.mainloop()
