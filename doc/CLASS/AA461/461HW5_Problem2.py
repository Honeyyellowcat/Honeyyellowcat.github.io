import math
import matplotlib.pyplot as plt

# Given parameters
hub_tip_ratio = 0.8
degree_of_reaction_mid_radius = 0.50

# Function to calculate axial velocity ratio
def axial_velocity_ratio(hub_tip_ratio):
    return (1 + hub_tip_ratio) / (1 - hub_tip_ratio)

# Function to calculate degree of reaction at hub radius
def degree_of_reaction_hub_radius(axial_velocity_ratio, degree_of_reaction_mid_radius):
    return 2 * degree_of_reaction_mid_radius / (1 + axial_velocity_ratio)

# Calculate axial velocity ratio U2/U1
axial_velocity_ratio = axial_velocity_ratio(hub_tip_ratio)

# Calculate rotor blade angles at hub radius
beta_2h = math.radians(90)  # Assuming beta_2h is 90 degrees (a rough approximation)
degree_of_reaction_hub = degree_of_reaction_hub_radius(axial_velocity_ratio, degree_of_reaction_mid_radius)
beta_3h = math.atan((1 - degree_of_reaction_hub) / (axial_velocity_ratio * math.tan(beta_2h)))

# Print calculated values
print("Axial velocity ratio U2/U1:", axial_velocity_ratio)
print("Rotor blade angle beta_3^h (at hub radius):", math.degrees(beta_3h))
print("Degree of reaction at hub radius:", degree_of_reaction_hub)

# Define points and labels
points = {
    'stator': (0, 0),
    'rotor': (5, 0),
    'w1': (2, 2),
    'w2': (3, -1),
    'v1': (2, 3),
    'v2': (4, 1)
}

labels = {
    'w1': 'W1* (Relative Velocity)',
    'w2': 'W2* (Relative Velocity)',
    'v1': 'V1* (Absolute Velocity)',
    'v2': 'V2* (Absolute Velocity)'
}

# Plotting the velocity triangles
fig, ax = plt.subplots()

# Plot lines
ax.plot([points['stator'][0], points['w1'][0]], [points['stator'][1], points['w1'][1]], 'r--')
ax.plot([points['stator'][0], points['v1'][0]], [points['stator'][1], points['v1'][1]], 'b--')
ax.plot([points['w1'][0], points['rotor'][0]], [points['w1'][1], points['rotor'][1]], 'r--')
ax.plot([points['v1'][0], points['rotor'][0]], [points['v1'][1], points['rotor'][1]], 'b--')

ax.plot([points['rotor'][0], points['w2'][0]], [points['rotor'][1], points['w2'][1]], 'r--')
ax.plot([points['rotor'][0], points['v2'][0]], [points['rotor'][1], points['v2'][1]], 'b--')
ax.plot([points['w2'][0], points['stator'][0]], [points['w2'][1], points['stator'][1]], 'r--')
ax.plot([points['v2'][0], points['stator'][0]], [points['v2'][1], points['stator'][1]], 'b--')

# Add labels
for point, coord in points.items():
    ax.text(coord[0], coord[1], f'{point}', verticalalignment='bottom' if coord[1] >= 0 else 'top', horizontalalignment='right' if coord[0] >= 0 else 'left')

for label, coord in points.items():
    if label in labels:
        ax.text(coord[0], coord[1], f'{labels[label]}', verticalalignment='bottom' if coord[1] >= 0 else 'top', horizontalalignment='right' if coord[0] >= 0 else 'left', color='red' if 'w' in label else 'blue')

# Set axis limits and labels
ax.set_xlim(-1, 6)
ax.set_ylim(-2, 4)
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('Axial Direction')
ax.set_ylabel('Tangential Direction')

plt.title('Velocity Triangles')
plt.grid()
plt.show()
