# Given values for part A
N1 = 15200  # rpm
m1 = 30.1   # kg/s
PR1 = 585 / 102  # pressure ratio
T1 = 20 + 273.15  # initial temperature in Kelvin
P_ambient = 102  # kPa
T_ambient = 20 + 273.15  # ambient temperature in Kelvin
P_standard = 101  # kPa
T_standard = 15 + 273.15  # standard temperature in Kelvin

# Calculations for part A
# Shaft Rotation Speed (N2)
N2 = N1 * (T_standard / T1)**0.5

# Air Density at ambient and standard conditions
rho_ambient = P_ambient / (287.05 * T_ambient)
rho_standard = P_standard / (287.05 * T_standard)

# Mass Flow Rate (m2)
m2 = m1 * (rho_standard / rho_ambient)

# Pressure Ratio (PR2)
PR2 = PR1 * (T_standard / T1)

# Results for part A
print("Part A Results:")
print(f"Shaft Rotation Speed (N2): {N2:.2f} rpm")
print(f"Mass Flow Rate (m2): {m2:.2f} kg/s")
print(f"Pressure Ratio (PR2): {PR2:.2f}")
print("\n")

# Given values for part B
P_ambient_modified = 86.4  # kPa
T_ambient_modified = 27 + 273.15  # modified ambient temperature in Kelvin
m3_measured = 27.2  # kg/s
P_exit_modified = 526.5  # kPa

# Air Density at modified conditions
rho_ambient_modified = P_ambient_modified / (287.05 * T_ambient_modified)

# Calculations for part B
# Shaft Rotation Speed (N3)
N3 = N1 * (T_ambient_modified / T1)**0.5

# Mass Flow Rate (m3)
rho_modified = P_exit_modified / (287.05 * T_ambient_modified)
m3_calculated = m1 * (rho_modified / rho_ambient_modified)

# Pressure Ratio (PR3)
PR3 = PR1 * (T_ambient_modified / T1)

# Results for part B
print("Part B Results:")
print(f"Shaft Rotation Speed (N3): {N3:.2f} rpm")
print(f"Calculated Mass Flow Rate (m3): {m3_calculated:.2f} kg/s")
print(f"Measured Mass Flow Rate (m3): {m3_measured:.2f}")
print(f"Pressure Ratio (PR3): {PR3:.2f}")
