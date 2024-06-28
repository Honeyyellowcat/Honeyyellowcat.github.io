import math

# Given data
k = 5  # Thermal conductivity in W/m*K
L = 0.1  # Length of the heater in meters (100 mm converted to meters)
r_outer = 0.0025  # Outer radius of the heater in meters (5 mm converted to meters)
r_inner = 0.002  # Inner radius of the heater (2 mm smaller than outer radius, 0.002 meters)

Q = 50  # Rate of heat transfer in watts
T_surrounding = 25 + 273.15  # Surrounding temperature in Kelvin (25°C converted to Kelvin)

# Calculate the temperature difference
delta_T = Q * math.log(r_outer / r_inner) / (2 * math.pi * k * L)

# Calculate the temperature reached by the heater
T_heater = T_surrounding + delta_T

# Convert temperature back to Celsius for display
T_heater_Celsius = T_heater - 273.15

print(f"The temperature reached by the heater is approximately {T_heater_Celsius:.2f} °C.")
