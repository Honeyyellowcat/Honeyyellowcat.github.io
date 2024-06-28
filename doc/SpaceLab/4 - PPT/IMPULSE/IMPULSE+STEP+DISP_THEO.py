import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import step
from scipy import signal

# Given parameters
m_pendulum = 3.16  # mass of the pendulum (kg)
lever_arm = 18 * 0.0254  # length of lever arm (m)
impulse = 10e-6  # Impulse magnitude (N*s)
zeta = 0.2  # damping ratio

# Flexure dimensions
w = 0.75 * 0.0254  # width of flexures (m)
h = 0.01 * 0.0254  # thickness of flexures (m)
l = 1.64 * 0.0254  # length of flexures (m)

# Material properties
E_steel = 200e9  # Young's modulus of steel (Pa)

# Calculate equivalent spring constant of flexures
k = (3 * E_steel * w * h**3) / (4 * l**3)

# Calculate natural frequency and damping coefficient
omega_n = np.sqrt(k / m_pendulum)  # natural frequency (rad/s)
c = 2 * zeta * omega_n * m_pendulum  # damping coefficient (N*s/m)

# Calculate impulse force
duration = 0.00003  # duration of impulse (s)
F_impulse = impulse / duration  # impulse force (N)

# Time vector for plots
time = np.linspace(0, 0.1, 1000)  # Define time vector

# LVDT response to applied impulse
LVDT_response = F_impulse / (m_pendulum * omega_n**2) * (1 - np.exp(-zeta * omega_n * time) * np.cos(np.sqrt(1 - zeta**2) * omega_n * time))

# Maximum deflection vs. Impulse pulse width normalized by the natural period
impulse_pulse_width = np.linspace(0.01, 1, 100)
normalized_pulse_width = impulse_pulse_width * omega_n / (2 * np.pi)
max_deflection = (F_impulse / k) * (1 - np.exp(-zeta * omega_n * impulse_pulse_width) * np.cos(np.sqrt(1 - zeta**2) * omega_n * impulse_pulse_width))

# Calibration curve for initial velocity change due to impulse
applied_impulse = np.linspace(0.001, 0.02, 100)
initial_velocity_change = np.full_like(applied_impulse, F_impulse / m_pendulum * (1 - np.exp(-zeta * omega_n * duration) * np.cos(np.sqrt(1 - zeta**2) * omega_n * duration)))

# Parameters for the pulsed plasma thruster
m_thruster = 1.0  # mass of the thruster (kg)
c_thruster = 0.1  # damping coefficient of the thruster (N*s/m)
k_thruster = 100.0  # stiffness of the thruster (N/m)

# Transfer function representation of the pulsed plasma thruster system
num_thruster = [1]
den_thruster = [m_thruster, c_thruster, k_thruster]
sys_tf_thruster = signal.TransferFunction(num_thruster, den_thruster)

# Simulate the system's response to a step input
t_step, response_step = step(sys_tf_thruster)

# Define uncertainties for LVDT response
# Assuming you have some measurements or estimates for the uncertainty
LVDT_response_uncertainty = np.random.uniform(0.1, 0.2, size=len(time))  # Example uncertainty values

# Create a single figure with subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

# Plot the step response of the pulsed plasma thruster system
axs[2].plot(t_step, response_step, 'b', label='Step Response')
axs[2].set_title('Deflection vs. Time', fontsize=14)
axs[2].set_xlabel('Time (seconds)', fontsize=14)
axs[2].set_ylabel('Response', fontsize=14)
axs[2].legend()
axs[2].grid(True)

# Plot LVDT response to applied impulse with uncertainty
axs[1].plot(time, LVDT_response, color='blue', label='LVDT Response')
axs[1].fill_between(time, LVDT_response - LVDT_response_uncertainty, LVDT_response + LVDT_response_uncertainty, color='lightblue', alpha=0.3)
axs[1].set_title('Voltage vs. Time', fontsize=14)
axs[1].set_xlabel('Time (s)', fontsize=14)
axs[1].set_ylabel('Voltage', fontsize=14)
axs[1].legend()
axs[1].grid(True)

# Plot Maximum deflection vs. Impulse pulse width normalized by the natural period
axs[0].plot(normalized_pulse_width, max_deflection, color='red', label='Max Deflection')
axs[0].set_title('Impuse Responce', fontsize=14)
axs[0].set_xlabel('Time (s)', fontsize=14)
axs[0].set_ylabel('Deflection (m)', fontsize=14)
axs[0].legend()
axs[0].grid(True)

# Adjust layout and increase spacing between subplots
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.5, hspace=0.5)

plt.show()
