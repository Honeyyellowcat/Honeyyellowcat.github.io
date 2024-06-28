import tkinter as tk
from tkinter import ttk

def on_click_a():
    print("Calculate Constant C button clicked")

def on_click_b():
    print("Plot Linear Impulse button clicked")

def on_quit():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Calibration Interface")
root.configure(bg='#333')  # Set background color to dark gray

# Configure style
style = ttk.Style()
style.theme_use('clam')  # Using clam theme for better button appearance
style.configure('TButton', font=('Helvetica', 12), foreground='#3b5998')  # White text
style.map('TButton', foreground=[('pressed', 'black')])  # Change text color when pressed

# Create a frame for the Calibration section
calibration_frame = tk.Frame(root, bg='#333')
calibration_frame.pack(pady=20)

# Add a label for the Calibration header
calibration_label = tk.Label(calibration_frame, text="Calibration", font=("Helvetica", 24, "bold"), fg="#fff", bg='#333')
calibration_label.pack()

# Create a frame for the Calibration buttons
calibration_button_frame = tk.Frame(root, bg='#333')
calibration_button_frame.pack(pady=20)

# Add the 'Calculate Constant C' button
button_a = ttk.Button(calibration_button_frame, text="Calculate Constant C", width=20, command=on_click_a, style='TButton')
button_a.grid(row=0, column=0, padx=10)

# Add the 'Plot Linear Impulse' button
button_b = ttk.Button(calibration_button_frame, text="Plot: Linear Impulse", width=20, command=on_click_b, style='TButton')
button_b.grid(row=0, column=1, padx=10)

# Create a frame for the Test section
test_frame = tk.Frame(root, bg='#333')
test_frame.pack(pady=20)

# Add a label for the Test header
test_label = tk.Label(test_frame, text="Test", font=("Helvetica", 24, "bold"), fg="#fff", bg='#333')
test_label.pack()

# Create a frame for the Test buttons
test_button_frame = tk.Frame(root, bg='#333')
test_button_frame.pack(pady=20)

# Add the first button for the Test section
button_c = ttk.Button(test_button_frame, text="Plot: Thrusrter Impulse", width=20, command=on_click_a, style='TButton')
button_c.grid(row=0, column=0, padx=10)

# Add the second button for the Test section
button_d = ttk.Button(test_button_frame, text="Export Plots", width=20, command=on_click_b, style='TButton')
button_d.grid(row=0, column=1, padx=10)

# Add the 'Quit' button
button_quit = ttk.Button(root, text="Quit", width=10, command=on_quit, style='TButton')
button_quit.pack(pady=10)

# Run the main loop
root.mainloop()
