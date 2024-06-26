
import serial
import serial.tools.list_ports
import tkinter as tk

def move_custom(direction, steps):
    global current_position, step_counter_label  # variables global
    if direction == 'Forward':  # Check if the direction is forward
        current_position += steps  # Increment the current position by the number of steps
        ser.write(b'A' + str(steps).encode())  # Command for forward movement
    else:
        current_position -= steps 
        ser.write(b'B' + str(steps).encode())  # Command for backward movement
    step_counter_label.config(text=f"Step Count: {current_position}")  # Update the step counter

# Function to stop everything immediately
def stop_all():
   ser.write(b'S')  # Send the stop command to Arduino
   ser.flush()  # Flush the serial buffer to ensure the command is sent immediately

#Function to move motor to zero position
def move_to_zero():
    global current_position  # variable global
    steps_to_zero = -current_position  # Calculate the number of steps needed to move to position zero
    if steps_to_zero != 0:  # Check if there are steps needed to move to zero
        steps_to_zero -= current_position  # Decrement the current position by the number of steps
        ser.write(b'B' + str(abs(steps_to_zero)).encode())  # Command to move backward to zero position
        step_counter_label.config(text="Step Count: 0")

#Function to quit
def quit_app():
    move_to_zero() 
    ser.close()
    root.quit()
#GUI setup
def create_gui():
    global root, current_position, step_counter_label  # Declare root as a global variable
    root = tk.Tk()
    root.title("Stepper Motor Control")
    current_position = 0

    forward_button = tk.Button(root, text="Forward 100 steps", command=lambda: move_custom('Forward', 100))
    forward_button.grid(row=0, column=0, padx=10, pady=10)

    backward_button = tk.Button(root, text="Backward 100 steps", command=lambda: move_custom('Backward', 100))
    backward_button.grid(row=0, column=1, padx=10, pady=10)

    custom_button = tk.Button(root, text="Custom Steps", command=custom_steps)
    custom_button.grid(row=1, columnspan=2, padx=10, pady=10)

    quit_button = tk.Button(root, text="Quit", command=quit_app)
    quit_button.grid(row=2, columnspan=2, padx=10, pady=10)

    step_counter_label = tk.Label(root, text="Step Count: 0")
    step_counter_label.grid(row=3, columnspan=2, padx=10, pady=10)

    root.mainloop()

#Function for custom steps input
def custom_steps():
    custom_window = tk.Toplevel(root)
    custom_window.title("Custom Steps")

    direction_label = tk.Label(custom_window, text="Direction:")
    direction_label.grid(row=0, column=0, padx=10, pady=10)

    direction_var = tk.StringVar(value="Forward")
    direction_menu = tk.OptionMenu(custom_window, direction_var, "Forward", "Backward")
    direction_menu.grid(row=0, column=1, padx=10, pady=10)

    steps_label = tk.Label(custom_window, text="Steps:")
    steps_label.grid(row=1, column=0, padx=10, pady=10)

    steps_entry = tk.Entry(custom_window)
    steps_entry.grid(row=1, column=1, padx=10, pady=10)

    confirm_button = tk.Button(custom_window, text="Move", command=lambda: move_custom(direction_var.get(), int(steps_entry.get())))
    confirm_button.grid(row=2, columnspan=2, padx=10, pady=10)
#Arduino port
def get_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'COM3' in port.device: 
            return port.device
    return None

#Main
arduino_port = get_arduino_port()
if arduino_port:
    ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)
    create_gui()
else:
    print('Arduino not found on any port!')