import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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

# Define the system equations
def system_eqns(x, t, k, m, c, F):
    # State variables
    y, v = x

    # Derivatives
    dydt = v
    dvdt = (1 / m) * (F - k * y - c * v)

    return [dydt, dvdt]

# Simulate motion using odeint
t = np.linspace(0, 2, 1000)  # time span for simulation
x = odeint(system_eqns, [0, 0], t, args=(k, m_pendulum, c, F_impulse))[:, 0]

# Calculate 2% steady state
#steady_state = 0.02 * max(x)

# Find the peak displacement and its time
peak_index = np.argmax(x)
peak_time = t[peak_index]
peak_value = x[peak_index]

# Plot displacement vs time
plt.figure()
plt.plot(t, x, label='Pendulum Displacement')
plt.axhline(color='r', linestyle='--', label='2% Steady State')
plt.text(peak_time, peak_value, f'Peak: {peak_value:.2e} m', fontsize=10, ha='right')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Displacement vs Time 10\u03BCN*s Impulse on 0.01" Thick Flexures')
plt.grid(True)
plt.legend()
plt.show()
