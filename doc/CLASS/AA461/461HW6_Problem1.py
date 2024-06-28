import numpy as np
import matplotlib.pyplot as plt

# Given data
thickness_percent = 0.03
Reynolds_number = 1e5
Cd_cylinder = 1.0

# Function to calculate skin friction coefficient
def skin_friction_coefficient(Re):
    # Empirical relation for skin friction coefficient
    Cf = 0.074 / Re ** 0.2
    return Cf

# Calculate skin friction coefficient for the airfoil
Cf_airfoil = skin_friction_coefficient(Reynolds_number)

# Calculate drag coefficient for the airfoil (both upper and lower surfaces)
Cd_airfoil = 2 * Cf_airfoil

# Calculate the equivalent diameter for a circular cylinder with the same drag coefficient
diameter_cylinder = (Cd_airfoil / Cd_cylinder) ** 0.5

# Plot the shapes to scale
plt.figure(figsize=(10, 5))

# Airfoil shape
plt.subplot(1, 2, 1)
plt.plot([0, 1, 1, 0], [0, thickness_percent / 2, -thickness_percent / 2, 0], 'b-', label='Airfoil')
plt.axis('equal')
plt.title('Airfoil')
plt.xlabel('Chord')
plt.ylabel('Thickness')

# Circular cylinder shape
plt.subplot(1, 2, 2)
circle = plt.Circle((0.5, 0), diameter_cylinder / 2, color='r', fill=False)
plt.gca().add_patch(circle)
plt.axis('equal')
plt.title('Circular Cylinder')
plt.xlabel('Diameter')
plt.ylabel('Height')

plt.tight_layout()
plt.show()

# Output the diameter of the circular cylinder
print("Diameter of the circular cylinder with the same drag coefficient:", diameter_cylinder)
