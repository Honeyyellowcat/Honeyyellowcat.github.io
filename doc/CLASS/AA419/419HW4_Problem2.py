import numpy as np
from scipy.integrate import odeint

# Given parameters
D = 0.1  # diameter in meters
Ti = 50  # initial temperature in Celsius
T_infty = 20  # ambient temperature in Celsius
k = 2  # thermal conductivity in W/(m*K)
rho = 2500  # density in kg/m^3
cp = 750  # specific heat capacity in J/(kg*K)
h = 30  # convective heat transfer coefficient in W/(m^2*K)
T_surface = 26  # surface temperature in Celsius

# Calculations
V = (np.pi * D**3) / 6  # volume of the sphere
U = 4 * np.pi * (D/2)**2 / (np.pi * D**2)  # surface area-volume ratio

# Initial condition with linear temperature profile
r = np.linspace(0, D/2, 50)
T0 = Ti - (Ti - T_infty) * r / (D/2)

def model(T, t):
    dTdt = np.zeros_like(T)
    dTdt[0] = (k / (rho * cp)) * (1 / (D / 2)**2) * (T[1] - 2 * T[0] + Ti) - (2 * k / (D / 2)) * (T[0] - Ti) - h * U * (T[0] - T_infty) / (rho * cp * V)
    dTdt[1:-1] = (k / (rho * cp)) * (1 / (D / 2)**2) * (T[:-2] - 2 * T[1:-1] + T[2:])
    dTdt[-1] = (k / (rho * cp)) * (1 / (D / 2)**2) * (T[-2] - 2 * T[-1] + T_infty) - (2 * k / (D / 2)) * (T[-1] - Ti) - h * U * (T[-1] - T_infty) / (rho * cp * V)
    return dTdt

# Time points
t = np.linspace(0, 5000, 1000)  # time span

# Solve the ODE
T = odeint(model, T0, t)

# Find the time when the surface temperature reaches 26°C
idx = np.argmax(T[:, -1] >= T_surface)
time_reached = t[idx]

print("Time when the surface temperature reaches 26°C:", time_reached, "seconds")

# Calculate the energy transferred from the sphere at this time
energy_transferred = rho * cp * V * (Ti - T_surface)

print("Energy transferred from the sphere at this time:", energy_transferred, "Joules")
