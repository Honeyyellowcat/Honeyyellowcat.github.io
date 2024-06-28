# Given data
T_infinity_i = 22  # Interior air temperature in degrees Celsius
T_infinity_o = 0   # Exterior air temperature in degrees Celsius
hi = 5             # Inner convection heat transfer coefficient in W/(m^2*K)
ho = 30            # Outer convection heat transfer coefficient in W/(m^2*K)

# Original wall
Ls = 0.03           # Thickness of sheathing in meters
ks = 0.1            # Thermal conductivity of sheathing in W/(m^2*K)
A_original = 1      # Assume unit area for simplicity

# Retrofitted wall
Li = 0.03           # Thickness of extruded insulation in meters
ki = 0.029          # Thermal conductivity of insulation in W/(m^2*K)
Lg = 0.005          # Thickness of architectural glass in meters
kg = 1.4            # Thermal conductivity of glass in W/(m^2*K)
A_retrofitted = 1   # Assume unit area for simplicity

# Calculate thermal resistances
R_original = Ls / (ks * A_original)
R_insulation = Li / (ki * A_retrofitted)
R_glass = Lg / (kg * A_retrofitted)

# Sum of thermal resistances for each wall
sum_R_original = R_original + R_glass
sum_R_retrofitted = R_insulation + R_glass

# Calculate heat flux through the walls
Q_original = (T_infinity_i - T_infinity_o) / sum_R_original
Q_retrofitted = (T_infinity_i - T_infinity_o) / sum_R_retrofitted

# Display results
print(f"Heat flux through original wall: {Q_original:.2f} W/m^2")
print(f"Heat flux through retrofitted wall: {Q_retrofitted:.2f} W/m^2")
