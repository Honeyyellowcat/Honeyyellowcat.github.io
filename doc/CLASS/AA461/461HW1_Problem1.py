import matplotlib.pyplot as plt

def draw_velocity_diagram(rotation_direction, inlet_flow_direction, case_label):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Draw rotor and stator
    ax.arrow(0.5, 0.5, 0, 0.2 * rotation_direction, head_width=0.05, head_length=0.1, fc='black', ec='black')
    ax.plot([0.2, 0.8], [0.5, 0.5], 'k-', lw=2)
    
    # Draw inlet flow arrow
    ax.arrow(0.2, 0.5, 0.6 * inlet_flow_direction, 0, head_width=0.05, head_length=0.1, fc='blue', ec='blue')

    # Label the case
    ax.text(0.5, 0.9, f'Case {case_label}', ha='center', va='center', fontsize=12, bbox=dict(facecolor='white', edgecolor='white'))

    # Set plot limits and labels
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f'Rotation: {rotation_direction}, Inlet Flow: {inlet_flow_direction}')
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')

    plt.show()

# Case 1: Rotation downward, Inlet flow to the right
draw_velocity_diagram(rotation_direction=-1, inlet_flow_direction=1, case_label=1)

# Case 2: Rotation upward, Inlet flow to the left
draw_velocity_diagram(rotation_direction=1, inlet_flow_direction=-1, case_label=2)

# Case 3: Rotation downward, Inlet flow to the left
draw_velocity_diagram(rotation_direction=-1, inlet_flow_direction=-1, case_label=3)

# Case (b): Rotor downward, Stator curved lines lower left to upper right
fig, ax = plt.subplots(figsize=(8, 6))
ax.arrow(0.5, 0.5, 0, -0.2, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax.plot([0.2, 0.8], [0.5, 0.5], 'k-', lw=2)
ax.plot([0.2, 0.8], [0.3, 0.7], 'k-', lw=2)

# Label the case
ax.text(0.5, 0.9, '(b) Compressor Stage', ha='center', va='center', fontsize=12, bbox=dict(facecolor='white', edgecolor='white'))

# Set plot limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title('(b) Rotor: Downward, Stator: Curved lines lower left to upper right')
ax.set_aspect('equal', adjustable='box')
plt.axis('off')

plt.show()
