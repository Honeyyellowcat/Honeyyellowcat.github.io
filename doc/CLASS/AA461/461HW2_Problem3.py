import math

# Given values
alpha1_star = 30  # degrees
alpha1_star_rad = math.radians(alpha1_star)
phi = 30 - alpha1_star  # degrees

# Part-speed operation
c1a_star = 150 * math.cos(alpha1_star_rad)
c1a = 0.45 * c1a_star

# Solve for alpha1 at part-speed operation
alpha1_rad = math.acos(0.45)
alpha1_deg = math.degrees(alpha1_rad)

# Calculate the angular change in IGV
phi = alpha1_star - alpha1_deg

# Check the sign of phi to determine the required direction of IGV rotation
rotation_direction = "counterclockwise" if phi > 0 else "clockwise"

print(f"The amount of angular change in the IGV required is {phi:.2f} degrees.")
print(f"The required direction of IGV rotation is {rotation_direction}.")
