import math

# Constants
epsilon_p = 0.6  # Emissivity of the pipe
sigma = 5.67e-8  # Stefan-Boltzmann constant in W/m^2/K^4
T_pipe = 353     # Temperature of the pipe in Kelvin
T_ambient = 293  # Ambient temperature in Kelvin
cost_per_kWh = 0.10  # Cost per kWh
hours_per_day = 24    # Number of hours in a day

# Assuming the radius of the pipe (in meters)
radius = 0.05  # Example value, you should adjust as per your problem

# Surface area of the pipe per unit length (2*pi*r)
surface_area_per_length = 2 * math.pi * radius

# Calculate the rate of heat loss due to radiation
heat_loss_rate = epsilon_p * sigma * surface_area_per_length * (T_pipe**4 - T_ambient**4)

# Convert heat loss rate to kW/m
heat_loss_rate_kW_per_m = heat_loss_rate / 1000

# Calculate the daily cost of heat loss per unit length
daily_cost = heat_loss_rate_kW_per_m * hours_per_day * cost_per_kWh

print("Daily cost of heat loss per unit length of the uninsulated pipe: {:.10f} USD/m".format(daily_cost))
