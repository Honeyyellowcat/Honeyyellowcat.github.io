# Importing necessary libraries
import tkinter as tk  # Importing the tkinter library for GUI
from tkinter import ttk  # Importing themed widgets from tkinter for a modern look and feel
import numpy as np  # Importing numpy for numerical computing
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot for plotting and visualization
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Importing FigureCanvasTkAgg from matplotlib.backends.backend_tkagg for embedding matplotlib figures in Tkinter GUIs
from scipy.signal import impulse, find_peaks  # Importing impulse and find_peaks from scipy.signal for system analysis


def display_graph():
    # Parameters
    m_pendulum = 3.1591  # mass of the pendulum (kg)
    l = 0.4572  # length of the pendulum (m)
    g = 9.81  # gravity (m/s^2)
    G = 80e9  # shear modulus of spring steel from Matweb
    h = 0.041656  # effective height of flexure
    b = 0.000254 * 2  # thickness of flexure
    L = 0.01905  # width of flexure
    J = 1 / 12 * (b * h ** 3 + b ** 3 * h)  # polar moment of inertia of the flexure
    ks = G * J / L  # torsional stiffness of flexure
    theta0 = np.deg2rad(0.01)  # initial angular displacement (radians)
    omega0 = 0  # initial angular velocity (rad/s)
    impulse_magnitude = 10e-6  # Impulse magnitude in Newton-seconds

    # Convert initial angular displacement to linear displacement (small angle approximation)
    x0 = l * theta0  # initial linear displacement (m)
    v0 = l * omega0  # initial linear velocity (m/s)

    # Calculate equivalent spring constant (using small angle approximation)
    k_eq = ks - m_pendulum * g * l

    # Calculate damping coefficient based on the desired damping ratio (ζ)
    zeta = 0.3  # damping ratio
    c = 2 * zeta * np.sqrt(m_pendulum * k_eq)

    # Transfer function representation of the mass-spring-damper system
    num = [1]
    den = [m_pendulum, c, k_eq]
    sys_tf = (num, den)

    # Simulate the system's response to an impulse input
    t_impulse, response_impulse = impulse(sys_tf)

    # Find peaks in the response
    peaks, _ = find_peaks(response_impulse)

    # Create a tkinter GUI window
    root = tk.Tk()
    root.title("Impulse Response Plot")

    # Create a figure for plotting
    fig = plt.figure(figsize=(10, 6))
    plt.plot(t_impulse, response_impulse, 'b', label='Impulse Response')
    plt.title('Impulse Response of the System')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Response')
    plt.legend()
    plt.grid(True)

    # Label peaks and draw lines to response axes
    for peak in peaks:
        plt.plot(t_impulse[peak], response_impulse[peak], 'ro')  # Mark the peak
        plt.text(t_impulse[peak], response_impulse[peak], f'({t_impulse[peak]:.2f}, {response_impulse[peak]:.2f})', fontsize=9, verticalalignment='bottom')
        plt.plot([t_impulse[peak], t_impulse[peak]], [0, response_impulse[peak]], 'r--')

    # Embed the matplotlib figure in the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Function to quit the application
    def quit_app():
        root.quit()
        root.destroy()

    # Create a quit button
    quit_button = ttk.Button(root, text="Quit", command=quit_app)
    quit_button.pack(side=tk.BOTTOM)

    # Run the tkinter event loop
    tk.mainloop()


# Create a tkinter GUI window
root = tk.Tk()
root.title("Control Panel")

# Create a button to display the graph
display_button = ttk.Button(root, text="Display Graph", command=display_graph)
display_button.pack(side=tk.LEFT, padx=10, pady=10)

# Function to quit the application
def quit_app():
    root.quit()
    root.destroy()

# Create a quit button
quit_button = ttk.Button(root, text="Quit", command=quit_app)
quit_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the tkinter event loop
tk.mainloop()
