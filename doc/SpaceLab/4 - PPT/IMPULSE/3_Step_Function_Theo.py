import tkinter as tk # Importing the tkinter library for GUI DAQ_Python.py
from tkinter import ttk # Importing themed widgets from tkinter for a modern look and feel
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import step
from scipy import signal

# Parameters for the pulsed plasma thruster
# (replace these with your actual parameters)
m_thruster = 1.0  # mass of the thruster (kg)
c_thruster = 0.1  # damping coefficient of the thruster (N*s/m)
k_thruster = 100.0  # stiffness of the thruster (N/m)

# Transfer function representation of the pulsed plasma thruster system
# h(s) = (1) / (m_thruster^2 + c_thruster + k_thruster)
num_thruster = [1]
den_thruster = [m_thruster, c_thruster, k_thruster]
sys_tf_thruster = signal.TransferFunction(num_thruster, den_thruster)

# Simulate the system's response to a step input
t_step, response_step = step(sys_tf_thruster)

#def display_graph():
#    try:
        # Plot the step response
plt.figure(figsize=(10, 6))
plt.plot(t_step, response_step, 'b', label='Step Response')
plt.title('Step Response of the Pulsed Plasma Thruster System')
plt.xlabel('Time (seconds)')
plt.ylabel('Response')
plt.legend()
plt.grid(True)
plt.show()

#        # Display the plot
#        plt.show()

#    except Exception as e:
#        print(f"An error occurred during graph display: {e}")    

# Create main window
#root = tk.Tk()
#root.title("Deflection Data Analysis")

# Create frame for buttons
#button_frame = ttk.Frame(root)
#button_frame.pack(pady=5)

# Graph STEP RESPONCE 
#convert_button = ttk.Button(button_frame, text="Step Responce (m) V.S Time (s) Graph", command=display_graph)
#convert_button.grid(row=2, column=2, padx=9)

# Create quit button
#quit_button = ttk.Button(root, text="Quit", command=root.quit)
#quit_button.pack(pady=5)

#root.mainloop()