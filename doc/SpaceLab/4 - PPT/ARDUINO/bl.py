import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import time

def animate():
    x_data = np.arange(0, 10, 0.1)
    y_data = np.sin(x_data) + np.random.normal(0, 0.1, size=len(x_data))  # Add random noise
    
    line.set_data(x_data, y_data)
    ax.relim()
    ax.autoscale_view()
    ax.set_ylim(-10.5, 10.5)  # Set y-axis limits
    ax.set_xlim(x_data[0], x_data[-1])  # Set x-axis limits
    canvas.draw()
    
    root.after(50, animate)  # Update animation every 50 milliseconds

def on_click_a():
    print("Step Up button clicked")

def on_click_b():
    print("Step Down button clicked")

def quit_app():
    root.quit()
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Calibration Interface")
root.configure(bg='#333')  # Set background color to dark gray

# Configure style
style = ttk.Style()
style.theme_use('clam')  # Using clam theme for better button appearance
style.configure('TButton', font=('Helvetica', 12), foreground='#3b5998')  # White text
style.map('TButton', foreground=[('pressed', 'black')])  # Change text color when pressed

# Create a frame for the header
header_frame = tk.Frame(root, bg='#333')
header_frame.pack(pady=20)

# Add a label for the header
header_label = tk.Label(header_frame, text="Stepper Motor Calibration", font=("Helvetica", 24, "bold"), fg="#fff", bg='#333')
header_label.pack()

# Create a frame for the plot
plot_frame = tk.Frame(root, bg='#333')
plot_frame.pack(pady=20)

# Create a matplotlib figure and axis
fig = Figure(figsize=(6, 5), dpi=100)
ax = fig.add_subplot(111)
line, = ax.plot([], [], lw=2)
ax.set_xlabel('Time (s)', fontsize=12)  # Set x-axis label font size
ax.set_ylabel('Voltage (V)')

# Add horizontal line at y=0
ax.axhline(0, color='black', linewidth=0.5)

# Create a canvas to display the plot
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack(expand=True, padx=20, pady=20)  # Expand canvas and add padding

# Create a frame for the buttons
button_frame = tk.Frame(root, bg='#333')
button_frame.pack(pady=20)

# Add the 'Step Up' button
button_a = ttk.Button(button_frame, text="Step Up", width=20, command=on_click_a, style='TButton')
button_a.grid(row=0, column=0, padx=20)

# Add the 'Step Down' button
button_b = ttk.Button(button_frame, text="Step Down", width=20, command=on_click_b, style='TButton')
button_b.grid(row=0, column=1, padx=20)

# Add the 'Quit' button
button_quit = ttk.Button(button_frame, text="Quit", width=20, command=quit_app, style='TButton')
button_quit.grid(row=1, column=0, columnspan=2, pady=10)

# Start the animation
animate()

# Run the main loop
root.mainloop()
