import math

# Given data
Ts = 60 + 273.15  # Surface temperature in Kelvin
T_infinity = 20 + 273.15  # Fluid temperature in Kelvin
L = 0.10  # Length of the plate in meters
nu_water = 1.004 * 10**-6  # Kinematic viscosity of water at 20°C in m^2/s
beta_water = 2.207 * 10**-4  # Volumetric thermal expansion coefficient of water in 1/K
g = 9.81  # Acceleration due to gravity in m/s^2

# Calculate Grashof number
Gr = (g * beta_water * (Ts - T_infinity) * L**3) / nu_water**2

# Calculate boundary layer thickness
delta = 0.37 * (Gr / 4)**(1/4)

# Minimum spacing between plates (twice the boundary layer thickness)
minimum_spacing = 2 * delta

print("Grashof number:", Gr)
print("Boundary layer thickness:", delta, "m")
print("Minimum spacing between plates to prevent interference:", minimum_spacing, "m")
