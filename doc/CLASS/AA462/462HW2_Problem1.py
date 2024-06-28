import numpy as np
import matplotlib.pyplot as plt

# Given parameters
delta_v_required = 8000  # 8 km/s in m/s
specific_impulse = 350  # Isp in seconds
gravity_acceleration = 9.81  # g0 in m/s^2
initial_mass_constraint = 100000  # Initial launch mass constraint in kg
structural_factor = 0.2  # Es - structural factor

# Function to calculate payload mass for a given number of stages (Case a)
def calculate_payload_mass_case_a(num_stages):
    final_mass = initial_mass_constraint
    for _ in range(num_stages):
        final_mass /= (1 - structural_factor)

    payload_mass = final_mass * (1 - np.exp(-delta_v_required / (specific_impulse * gravity_acceleration)))
    return payload_mass

# Structural factors for each stage (Case b)
structural_factors = {1: 0.2, 2: 0.2, 3: 0.25, 4: 0.3, 5: 0.4}

# Function to calculate payload mass for a given number of stages and structural factors (Case b)
def calculate_payload_mass_case_b(num_stages, structural_factors):
    final_mass = initial_mass_constraint
    payload_factor = 1
    for i in range(1, num_stages + 1):
        final_mass /= (1 - structural_factors[i])
        payload_factor *= np.exp(-delta_v_required / (specific_impulse * gravity_acceleration))

    payload_mass = final_mass * payload_factor
    return payload_mass

# Calculate payload masses for different numbers of stages
num_stages_values = np.arange(1, 6)
payload_mass_values_a = [calculate_payload_mass_case_a(n) for n in num_stages_values]
payload_mass_values_b = [calculate_payload_mass_case_b(n, structural_factors) for n in num_stages_values]

# Plotting
plt.plot(num_stages_values, payload_mass_values_a, label='Case a')
plt.plot(num_stages_values, payload_mass_values_b, label='Case b')
plt.xlabel('Number of Stages (N)')
plt.ylabel('Payload Mass ($m_{pl}$) in kg')
plt.title('Payload Mass vs Number of Stages')
plt.legend()
plt.grid(True)
plt.show()
