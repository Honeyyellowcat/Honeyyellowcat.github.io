import serial
import time

# Define the serial port and baud rate
serial_port = 'COM3'  # Change this to the port your Arduino is connected to
baud_rate = 9600

# Open serial connection
ser = serial.Serial(serial_port, baud_rate)
time.sleep(2)  # Wait for Arduino to reset after opening the serial port

# Send commands to control the stepper motor
while True:
    command = input("Enter 'F' to move forward or 'B' to move backward: ")
    if command == 'F':
        ser.write(b'F')  # Send forward command
    elif command == 'B':
        ser.write(b'B')  # Send backward command
    else:
        print("Invalid command. Enter 'F' or 'B'.")

# Close serial connection
ser.close()
