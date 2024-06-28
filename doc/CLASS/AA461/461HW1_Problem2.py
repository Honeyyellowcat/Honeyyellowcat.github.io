import numpy as np
import matplotlib.pyplot as plt

# Given values
c1 = 150
alpha1 = 30
beta2 = 30

# Convert angles to radians
alpha1_rad = np.radians(alpha1)
beta2_rad = np.radians(beta2)

# Part a: Velocity Triangle Calculations
# ---------------------------------------

# Calculate alpha rp
w1x = c1 * np.sin(alpha1_rad)
alpha_rp = np.degrees(np.arctan(w1x / c1))

# Calculate w1
w1 = np.sqrt(c1**2 + w1x**2)

# Calculate w2
w2 = w1

# Calculate c2
c2 = w2 * np.cos(beta2_rad)

# Calculate beta1 and alpha2
beta1 = np.degrees(np.arctan(w1x / c1))
alpha2 = np.degrees(beta2_rad)  # Assuming no shock

# Print results for Part a
print("\nPart a: Velocity Triangle Calculations")
print(f"Alpha rp: {alpha_rp:.2f} degrees")
print(f"W1: {w1:.2f} m/s")
print(f"W2: {w2:.2f} m/s")
print(f"C2: {c2:.2f} m/s")
print(f"Beta1: {beta1:.2f} degrees")
print(f"Alpha2: {alpha2:.2f} degrees")

# Part b: Total Pressure Ratio Calculation
# -----------------------------------------

# Additional values for Part b
R = 287  # Specific gas constant
gamma = 1.4  # Ratio of specific heats

# Calculate temperatures for Part b
T0 = 300  # Inlet total temperature
T01 = T0 + (w1**2) / (2 * R)  # Stagnation temperature at inlet
T02 = T01  # Assuming isentropic process
T03 = T01 + (w1**2 - w2**2) / (2 * R)  # Stagnation temperature at outlet

# Calculate total pressure ratio for Part b
p03_p02 = (T03 / T02)**(gamma / (gamma - 1))

# Print results for Part b
print("\nPart b: Total Pressure Ratio Calculation")
print(f"Total Pressure Ratio (p03/p02): {p03_p02:.4f}")

# Create subplots for each velocity triangle
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Define functions to calculate coordinates of velocity triangles
def velocity_triangle(ax, alpha, beta, label_alpha, label_beta):
    ax.arrow(0, 0, np.cos(alpha), np.sin(alpha), head_width=0.1, head_length=0.1, fc='red', ec='red', label=label_alpha)
    ax.arrow(0, 0, -np.cos(beta), np.sin(beta), head_width=0.1, head_length=0.1, fc='blue', ec='blue', label=label_beta)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(0, 1.5)
    ax.set_aspect('equal', adjustable='box')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend()

# Inlet velocity triangle
velocity_triangle(ax1, alpha1_rad, beta1, r'$\alpha_1$', r'$\beta_1$')
ax1.set_title('Inlet Velocity Triangle')

# Outlet velocity triangle
velocity_triangle(ax2, alpha_rp, beta2_rad, r'$\alpha_{rp}$', r'$\beta_2$')
ax2.set_title('Outlet Velocity Triangle')

plt.tight_layout()
plt.show()

# Part c: Downstream Total Temperature Calculation
# ------------------------------------------------

# Print result for Part c
print("\nPart c: Downstream Total Temperature Calculation")
print(f"Downstream Total Temperature (T03): {T03:.2f} K")

# Create subplots for each velocity triangle
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Define functions to calculate coordinates of velocity triangles
def velocity_triangle(ax, alpha, beta, label_alpha, label_beta):
    ax.arrow(0, 0, np.cos(alpha), np.sin(alpha), head_width=0.1, head_length=0.1, fc='red', ec='red', label=label_alpha)
    ax.arrow(0, 0, -np.cos(beta), np.sin(beta), head_width=0.1, head_length=0.1, fc='blue', ec='blue', label=label_beta)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(0, 1.5)
    ax.set_aspect('equal', adjustable='box')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend()

# Inlet velocity triangle
velocity_triangle(ax1, alpha1_rad, beta1, r'$\alpha_1$', r'$\beta_1$')
ax1.set_title('Inlet Velocity Triangle')

# Outlet velocity triangle
velocity_triangle(ax2, alpha_rp, beta2_rad, r'$\alpha_{rp}$', r'$\beta_2$')
ax2.set_title('Outlet Velocity Triangle')

plt.tight_layout()
plt.show()