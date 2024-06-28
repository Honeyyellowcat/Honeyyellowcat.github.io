import numpy as np

# Given data
Reynolds_number = 1e5

# Function to calculate skin friction coefficient
def skin_friction_coefficient(Re):
    # Empirical relation for skin friction coefficient
    Cf = 0.074 / Re ** 0.2
    return Cf

# Calculate skin friction coefficient for the airfoil
Cf_airfoil = skin_friction_coefficient(Reynolds_number)

# Calculate skin friction coefficient for the circular cylinder
Cf_cylinder = Cf_airfoil  # Assuming same skin friction coefficient for cylinder and airfoil

# Since heat transfer coefficient is proportional to skin friction coefficient
# Let's assume that the ratio d/c is also proportional to the ratio of skin friction coefficients
ratio_dc = (Cf_cylinder / Cf_airfoil)**0.5

print("Ratio d/c required to achieve the same rate of heat transfer:", ratio_dc)
