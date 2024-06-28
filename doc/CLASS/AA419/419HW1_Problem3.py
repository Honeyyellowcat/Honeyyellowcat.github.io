# Given values
T_skin = 37  # Skin temperature in °C
A = 2  # Surface area in square meters
T_ambient = 0  # Ambient temperature in °C
d = 0.01  # Insulation thickness in meters (1 cm converted to meters)
RMR = 100  # Resting metabolic rate in Watts

# Convert temperatures to Kelvin
T_skin_K = T_skin + 273.15
T_ambient_K = T_ambient + 273.15

# Calculate temperature difference
delta_T = T_skin_K - T_ambient_K

# Thermal conductivity of still air (assumed value for insulation)
k_air = 0.0257  # W/m·K

# Calculate heat flow using the steady-state heat conduction equation
heat_flow = (k_air * A * delta_T) / d

# Compare with resting metabolic rate
comparison = heat_flow / RMR

# Display the results
print(f"Estimated Heat Flow: {heat_flow:.2f} Watts")
print(f"Comparison with Resting Metabolic Rate: {comparison:.2%}")
