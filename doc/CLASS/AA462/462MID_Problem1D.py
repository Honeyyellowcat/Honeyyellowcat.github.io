import numpy as np
import matplotlib.pyplot as plt

# Given values
m2 = 0.24  # mass of the second stage

# Function to calculate the cost per launch given mass of first stage (example function, you can replace it with actual data/function)
def calculate_cost_per_launch(m1):
    # Example function, replace with actual cost calculation
    # Assuming a linear relationship between cost and mass of the first stage
    fixed_cost = 60e6  # $60 million USD (fixed cost)
    variable_cost_per_kg = 0.8e6  # $0.8 million USD per kg (variable cost)
    total_cost = fixed_cost + variable_cost_per_kg * (m1 + m2)
    return total_cost

# Mass range for the first stage
m1_values = np.linspace(0, 200, 100)  # Range of masses for the first stage

# Calculate cost per launch for each mass of the first stage
costs_per_launch = [calculate_cost_per_launch(m1) for m1 in m1_values]

# Plot
plt.plot(m1_values, costs_per_launch)
plt.xlabel('Mass of first stage ($m_1$) in kg')
plt.ylabel('Cost per launch ($C$) in USD')
plt.title('Cost per launch vs. Mass of first stage')
plt.grid(True)
plt.show()

# Check if cost per launch goal can be achieved and calculate number of reuses needed
cost_per_launch_goal = 100e6  # $100 million USD
if min(costs_per_launch) < cost_per_launch_goal:
    min_cost_index = np.argmin(costs_per_launch)
    min_cost_m1 = m1_values[min_cost_index]
    reuses_needed = (calculate_cost_per_launch(0) - cost_per_launch_goal) / (calculate_cost_per_launch(0) - calculate_cost_per_launch(min_cost_m1))
    print(f"We can achieve a cost per launch below ${cost_per_launch_goal/1e6:.2f} million USD.")
    print(f"To achieve this, we need to reuse our first stage approximately {reuses_needed:.2f} times.")
else:
    print("We cannot achieve a cost per launch below $100 million USD.")

# Analyze diminishing returns (dummy analysis)
# This can be based on the rate of decrease in cost per launch vs. the increase in reusability
# It depends on the actual cost function and other factors.
# For simplicity, let's just output a message indicating that there might be diminishing returns.
print("There might be a point of diminishing returns for reusability.")
