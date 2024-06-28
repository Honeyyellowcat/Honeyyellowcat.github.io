import math

# Given values
number_of_blades = 65 * 12 * 10
solidity_mean_diameter = 1.0
reaction = 0.5
axial_velocity_ratio = 0.5
beta_i_1_C_s1 = 65
beta_ii_1_C_s1 = 35
beta_i_1_C_s1_5 = 65
beta_ii_1_C_s1_5 = 52

# Constants
R = reaction

# Check if axial velocity ratio is not equal to zero
if axial_velocity_ratio == 0:
    raise ValueError("Axial velocity ratio (C_1) cannot be zero.")

# Step 1: Calculate Stator Flow Angle (beta_1)
C_a1_C_s1 = math.tan(math.radians(beta_ii_1_C_s1)) / math.tan(math.radians(beta_i_1_C_s1))
C_1 = C_a1_C_s1 / (1 - axial_velocity_ratio)  # Adjusted C_1
beta_1 = math.degrees(math.atan(math.atan((2 * R * (1 - R)) / (1 - C_a1_C_s1 / C_1))))

# Step 2: Calculate Rotor Flow Angle (beta_2)
C_a2_C_s1_5 = math.tan(math.radians(beta_ii_1_C_s1_5)) / math.tan(math.radians(beta_i_1_C_s1_5))
beta_2 = math.degrees(math.atan(math.atan((2 * R * (1 - R)) / (1 + C_a2_C_s1_5 / axial_velocity_ratio))))

# Step 3: Choose Stagger Angle (beta_s)
beta_s = (beta_1 + beta_2) / 2

# Display results
print(f"Stator Flow Angle (beta_1): {beta_1:.2f} degrees")
print(f"Rotor Flow Angle (beta_2): {beta_2:.2f} degrees")
print(f"Stagger Angle (beta_s): {beta_s:.2f} degrees")
