import serial
import serial.tools.list_ports
import tkinter as tk

# Function to move the stepper motor forward by 100 steps
def move_forward():
    ser.write(b'A')

# Function to move the stepper motor backward by 100 steps
def move_backward():
    ser.write(b'B')

# Function to quit the application
def quit_app():
    ser.close()  # Close the serial connection
    root.quit()  # Quit the Tkinter application

# GUI setup
def create_gui():
    global root  # Declare root as a global variable
    root = tk.Tk()
    root.title("Stepper Motor Control")

    forward_button = tk.Button(root, text="Forward 100 steps", command=move_forward)
    forward_button.grid(row=0, column=0, padx=10, pady=10)

    backward_button = tk.Button(root, text="Backward 100 steps", command=move_backward)
    backward_button.grid(row=0, column=1, padx=10, pady=10)

    quit_button = tk.Button(root, text="Quit", command=quit_app)
    quit_button.grid(row=1, columnspan=2, padx=10, pady=10)

    root.mainloop()

# Get the Arduino port
def get_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'COM3' in port.device:  # Adjust COM port according to your setup
            return port.device
    return None

# Main
arduino_port = get_arduino_port()
if arduino_port:
    ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)
    create_gui()
#else:
#    print('Arduino not found on any port!')
