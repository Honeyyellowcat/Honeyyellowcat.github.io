import pyfirmata
import tkinter as tk
from PIL import Image, ImageTk
import time

# CLOCKWISE and ANTICLOCKWISE rotation
def rotate_clockwise():
    board.digital[13].write(1)
    root.after(500, stop_motor)
def rotate_anticlockwise():
    board.digital[13].write(0)
    root.after(500, stop_motor)

# STOP the motor
def stop_motor():
    board.digital[13].write(0)

# QUIT the application
def quit_application():
    root.destroy()

# Board initialization
board = pyfirmata.Arduino("COM3")  

# GUI initialization
root = tk.Tk()
root.title("Arduino Controller")

# Canvas setup
canvas_width = 600
canvas_height = 450
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Load image
motor_img = Image.open("StepperMotor_ROHS.png")
motor_img = motor_img.resize((canvas_width, canvas_height), Image.ANTIALIAS)
motor_img = ImageTk.PhotoImage(motor_img)
canvas.create_image(canvas_width/2, canvas_height/2, image=motor_img)

# Buttons
btn_forward = tk.Button(root, text="Step down", command=rotate_clockwise)
btn_forward.grid(row=1, column=0, padx=10, pady=10)

btn_backward = tk.Button(root, text="Step up", command=rotate_anticlockwise)
btn_backward.grid(row=1, column=1, padx=10, pady=10)

btn_quit = tk.Button(root, text="Quit", command=quit_application)
btn_quit.grid(row=2, column=0, columnspan=2, pady=10)

# Start Tkinter main loop
root.mainloop()