import serial.tools.list_ports
import sys
import tkinter as tk

# Define pin numbers
pulPin = 2
dirPin = 3
enPin = 4

def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports

def find_arduino(ports_found):
    for port in ports_found:
        if 'COM3' in port.device:  # Adjust COM port according to your setup
            return port.device
    return None

def move_100_steps(connect_port):
    move_steps(connect_port, 100)

def move_steps(connect_port, steps):
    try:
        ser = serial.Serial(connect_port, baudrate=9600, timeout=1)
        print(f"Moved {steps} steps")
        ser.write(f'M{steps}\n'.encode())  # Send the number of steps prefixed with 'M'
        ser.close()  # Close serial connection
    except Exception as e:
        print('Error:', e)

def forward(connect_port, steps):
    try:
        ser = serial.Serial(connect_port, baudrate=9600, timeout=1)
        print(f"Forward {steps} steps")
        ser.write(f'F{steps}\n'.encode())  # Send the number of steps prefixed with 'F'
        ser.close()  # Close serial connection
    except Exception as e:
        print('Error:', e)

def backward(connect_port, steps):
    try:
        ser = serial.Serial(connect_port, baudrate=9600, timeout=1)
        print(f"Backward {steps} steps")
        ser.write(f'B{steps}\n'.encode())  # Send the number of steps prefixed with 'B'
        ser.close()  # Close serial connection
    except Exception as e:
        print('Error:', e)

def stop(connect_port):
    try:
        ser = serial.Serial(connect_port, baudrate=9600, timeout=1)
        print("Stop")
        ser.write(b'S\n')  # Send 'S' command to stop the motor
        ser.close()  # Close serial connection
    except Exception as e:
        print('Error:', e)

def quit_app():
    sys.exit()

# GUI setup
def create_gui(connect_port):
    root = tk.Tk()
    root.title("Stepper Motor Control")

    forward_button = tk.Button(root, text="Forward 100 steps", command=lambda: forward(connect_port, 100))
    forward_button.grid(row=0, column=0, padx=10, pady=10)

    backward_button = tk.Button(root, text="Backward 100 steps", command=lambda: backward(connect_port, 100))
    backward_button.grid(row=0, column=1, padx=10, pady=10)

    custom_move_button = tk.Button(root, text="Custom Move", command=lambda: move_steps(connect_port, int(custom_entry.get())))
    custom_move_button.grid(row=1, column=0, padx=10, pady=10)

    custom_entry = tk.Entry(root)
    custom_entry.grid(row=1, column=1, padx=10, pady=10)

    quit_button = tk.Button(root, text="Quit", command=quit_app)
    quit_button.grid(row=3, columnspan=2, padx=10, pady=10)

    root.mainloop()

found_ports = get_ports()
for port in found_ports:
    print(port)

connect_port = find_arduino(found_ports)
if connect_port:
    create_gui(connect_port)
else:
    print('Arduino not found on any port!')
    sys.exit(1)
