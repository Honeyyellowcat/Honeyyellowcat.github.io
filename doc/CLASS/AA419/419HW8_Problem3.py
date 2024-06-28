import math

# Given constants
sigma = 5.67e-8  # Stefan-Boltzmann constant in W/m^2/K
power_radiated = 100  # Power radiated in watts
surface_area = 2  # Surface area in square meters

# Calculate surface temperature in Kelvin
T = (power_radiated / (sigma * surface_area)) ** (1/4)

print("Surface temperature required to radiate 100W:", T, "K")
