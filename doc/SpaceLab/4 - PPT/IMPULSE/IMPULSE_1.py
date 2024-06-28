import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import impulse
from scipy import signal

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
sys_tf = signal.TransferFunction(num, den)

# Simulate the system's response to an impulse input
t_impulse, response_impulse = impulse(sys_tf, T=np.linspace(0, 2, 1000))

# Plot the impulse response
plt.figure(figsize=(10, 6))
plt.plot(t_impulse, response_impulse, 'b', label='Impulse Response')
plt.title('Impulse Response of the System')
plt.xlabel('Time (seconds)')
plt.ylabel('Response')
plt.legend()
plt.grid(True)
plt.show()