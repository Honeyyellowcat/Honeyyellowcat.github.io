import math

# Given data for part (a)
c_star = 1700  # m/s
gamma = 1.2
P_c = 2e6  # Pa
E = 25
throat_diameter = 0.1  # m

# Constants
R = 287  # J/(kg*K), specific gas constant for dry air
g_0 = 9.81  # m/s^2, acceleration due to gravity

# Calculating chamber density (rho_c)
T_c = P_c / (R * (gamma - 1))  # chamber temperature
rho_c = P_c / (R * T_c)  # chamber density

# Calculating throat area (A_t)
throat_radius = throat_diameter / 2
A_t = math.pi * throat_radius**2

# Calculating exit area (A_e)
A_e = E * A_t

# Calculating exit Mach number (M_e)
M_e = math.sqrt((2 / (gamma - 1)) * ((P_c / (rho_c * R))**((gamma - 1) / gamma) - 1))

# Calculating exit pressure (P_e)
P_e = P_c / ((1 + 0.5 * (gamma - 1) * M_e**2)**(gamma / (gamma - 1)))

# Calculating mass flow rate (dot_m)
dot_m = rho_c * A_t * c_star

# Calculating thrust (F)
F = dot_m * c_star + (P_e - 101325) * A_e  # Assuming ambient pressure is 101325 Pa

# Calculating thrust coefficient (C_f)
C_f = (2 / gamma / M_e**2) * (((2 / (gamma + 1)) * (1 + 0.5 * (gamma - 1) * M_e**2))**((gamma + 1) / (gamma - 1))) - (101325 / P_c) * A_e / A_t

# Calculating specific impulse (I_sp)
I_sp = c_star / g_0 * C_f

# Displaying the results for part (a)
print(f"Results for Part (a) - Vacuum:")
print(f"Mass Flow Rate (dot_m): {dot_m:.2f} kg/s")
print(f"Thrust (F): {F:.2f} N")
print(f"Thrust Coefficient (C_f): {C_f:.4f}")
print(f"Specific Impulse (I_sp): {I_sp:.2f} s")

# Given data for part (b)
ambient_pressure_sea_level = 101325  # Pa, standard sea-level pressure

# Calculating exit pressure at sea-level (P_e_sea_level)
P_e_sea_level = ambient_pressure_sea_level

# Calculating thrust at sea-level (F_sea_level)
F_sea_level = dot_m * c_star + (P_e_sea_level - ambient_pressure_sea_level) * A_e

# Calculating thrust coefficient at sea-level (C_f_sea_level)
C_f_sea_level = (2 / gamma / M_e**2) * (((2 / (gamma + 1)) * (1 + 0.5 * (gamma - 1) * M_e**2))**((gamma + 1) / (gamma - 1))) - (ambient_pressure_sea_level / P_c) * A_e / A_t

# Calculating specific impulse at sea-level (I_sp_sea_level)
I_sp_sea_level = c_star / g_0 * C_f_sea_level

# Displaying the results for part (b)
print("\nResults for Part (b) - Sea-Level:")
print(f"Thrust (F): {F_sea_level:.2f} N")
print(f"Thrust Coefficient (C_f): {C_f_sea_level:.4f}")
print(f"Specific Impulse (I_sp): {I_sp_sea_level:.2f} s")
