import matplotlib.pyplot as plt

# Define points and labels
points = {
    'V1*': (0, 0),
    'W1*': (2, 2),
    'W2*': (3, -1),
    'V2*': (5, -1),  # Adjusted V2* coordinates
    'Rotor': (2.5, 0)
}

labels = {
    'W1*': 'W1* (Relative Velocity)',
    'W2*': 'W2* (Relative Velocity)',
    'V1*': 'V1* (Absolute Velocity)',
    'V2*': 'V2* (Absolute Velocity)',
    'Rotor': 'Rotor (U*)'
}

# Plotting the velocity triangles
fig, ax = plt.subplots()

# Plot lines
ax.plot([points['V1*'][0], points['W1*'][0]], [points['V1*'][1], points['W1*'][1]], 'r--')
ax.plot([points['V1*'][0], points['Rotor'][0]], [points['V1*'][1], points['Rotor'][1]], 'b--')
ax.plot([points['W1*'][0], points['Rotor'][0]], [points['W1*'][1], points['Rotor'][1]], 'r--')
ax.plot([points['Rotor'][0], points['W2*'][0]], [points['Rotor'][1], points['W2*'][1]], 'r--')
ax.plot([points['Rotor'][0], points['V2*'][0]], [points['Rotor'][1], points['V2*'][1]], 'b--')
ax.plot([points['W2*'][0], points['V2*'][0]], [points['W2*'][1], points['V2*'][1]], 'r--')

# Add labels
for point, coord in points.items():
    ax.text(coord[0], coord[1], f'{point}', verticalalignment='bottom' if coord[1] >= 0 else 'top', horizontalalignment='right' if coord[0] >= 0 else 'left')

for label, coord in points.items():
    if label in labels:
        ax.text(coord[0], coord[1], f'{labels[label]}', verticalalignment='bottom' if coord[1] >= 0 else 'top', horizontalalignment='right' if coord[0] >= 0 else 'left', color='red' if 'W' in label else 'blue')

# Set axis limits and labels
ax.set_xlim(-1, 6)
ax.set_ylim(-2, 3)
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('Axial Direction')
ax.set_ylabel('Tangential Direction')

plt.title('Velocity Triangles')
plt.grid()
plt.show()
