# Given values
T_glass0 = 273  # Reference temperature for soda lime glass in Kelvin
T = 300  # Temperature for which we want to find k_glass
A_window = (400 / 1000) * (400 / 1000)  # Area of the window in square meters
delta_T = 90  # Temperature difference
L_pc = 0.012  # Thickness of poly-carbonate window in meters
L_glass = 0.012  # Thickness of soda lime glass window in meters
L_ag = 0.012  # Thickness of aerogel window in meters
k_pc = 0.21  # Thermal conductivity of poly-carbonate in W/m·K
k_ag = 0.014  # Thermal conductivity of aerogel in W/m·K
alpha_glass = 0.000004  # Temperature coefficient of thermal conductivity for soda lime glass
k_glass0 = 0.8  # Thermal conductivity of soda lime glass at reference temperature in W/m·K
num_windows = 130  # Number of windows
flight_duration = 8  # Flight duration in hours
cost_to_heat_air = 1  # Cost to heat the cabin air in $/kW·h

# Calculate thermal conductivity of soda lime glass at 300 K
k_glass = k_glass0 * (1 + alpha_glass * (T - T_glass0))

# Calculate heat loss rates
Q_pc = (k_pc * A_window * delta_T) / L_pc
Q_glass = (k_glass * A_window * delta_T) / L_glass
Q_ag = (k_ag * A_window * delta_T) / L_ag

# Calculate total cost for heat loss during the flight
total_cost = (Q_pc + Q_glass + Q_ag) * flight_duration * num_windows * cost_to_heat_air

# Display the results
print(f"Thermal conductivity of soda lime glass at 300 K: {k_glass} W/m·K")
print(f"Heat loss rate through poly-carbonate window: {Q_pc} Watts")
print(f"Heat loss rate through soda lime glass window: {Q_glass} Watts")
print(f"Heat loss rate through aerogel window: {Q_ag} Watts")
print(f"Total cost for heat loss during the flight: ${total_cost}")
