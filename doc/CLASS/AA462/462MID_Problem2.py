import math

# Given data
P_amb = 2e3  # Ambient pressure on Mars surface in Pa
T_amb = 220   # Ambient temperature on Mars surface in K
g_Mars = 0.38 * 9.81  # Gravitational acceleration on Mars in m/s^2
R = 8314.3 / (22 * 1000)  # Specific gas constant for Mars atmosphere in J/(kg K)
c_star = 1700  # Characteristic velocity in m/s
gamma = 1.2  # Specific heat ratio
M = 22  # Molar mass in AMU
P_c = 0.9e6  # Chamber pressure in Pa

# Calculate ambient density
rho_amb = P_amb / (R * T_amb)

# Calculate specific impulse
g_0 = 9.81  # Standard gravity in m/s^2
I_sp = c_star / g_0

# Calculate expansion ratio
epsilon = (P_c / P_amb) ** (1 / gamma)

# Calculate throat area
dot_m = P_c / math.sqrt(T_amb)
A_t = dot_m / rho_amb

# Calculate exit area
A_e = epsilon * A_t

# Calculate throat diameter (assuming circular cross-section)
d_t = (4 * A_t / math.pi) ** 0.5

# Calculate exit diameter (assuming circular cross-section)
d_e = (4 * A_e / math.pi) ** 0.5

# Display the results
print("a) Maximum expansion ratio (epsilon):", epsilon)
print("b) Throat diameter (d_t):", d_t, "m")
print("   Exit diameter (d_e):", d_e, "m")
