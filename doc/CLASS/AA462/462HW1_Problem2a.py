import numpy as np
import matplotlib.pyplot as plt

# Constants
I_sp = 450  # specific impulse in seconds
g_0 = 9.81  # acceleration due to gravity in m/s^2
nu_max_initial = 1.1
nu_max_max = 4.0

# Function to calculate ideal delta v
def delta_v_ideal(eta_0):
    return I_sp * g_0 * np.log(1 / (1 - eta_0))

# Function to calculate delta v for a given eta_0
def delta_v(eta_0):
    return I_sp * g_0 * np.log(1 / (1 - eta_0))

# Generate values for eta_0
eta_0_values = np.linspace(0.01, 0.99, 100)

# Calculate corresponding delta v values
delta_v_ideal_values = delta_v_ideal(eta_0_values)
delta_v_initial_values = delta_v(0.1)
delta_v_max_values = delta_v(1 / nu_max_max)

# Plotting
plt.figure(figsize=(10, 6))

# i. Delta v_ideal vs. eta_0
plt.subplot(221)
plt.plot(eta_0_values, delta_v_ideal_values, label=r'$\Delta v_{\text{ideal}}$')
plt.xlabel(r'$\eta_0$')
plt.ylabel(r'$\Delta v_{\text{ideal}}$')
plt.legend()

# ii. Delta v vs. eta_0 for eta_0 = 1.1
plt.subplot(222)
plt.plot(eta_0_values, delta_v_initial_values * np.ones_like(eta_0_values), label=r'$\eta_0 = 1.1$')
plt.xlabel(r'$\eta_0$')
plt.ylabel(r'$\Delta v$')
plt.legend()

# iii. Delta v vs. eta_0 for eta_max = 4
plt.subplot(223)
plt.plot(eta_0_values, delta_v_max_values * np.ones_like(eta_0_values), label=r'$\eta_{\text{max}} = 4$')
plt.xlabel(r'$\eta_0$')
plt.ylabel(r'$\Delta v$')
plt.legend()

# iv. Highlight feasible region
plt.subplot(224)
plt.fill_between(eta_0_values, delta_v_initial_values, delta_v_max_values, color='gray', alpha=0.3, label='Feasible Region')
plt.xlabel(r'$\eta_0$')
plt.ylabel(r'$\Delta v$')
plt.legend()

# Save the plot to an image file
plt.tight_layout()
plt.savefig('problem2_plots.png')
plt.show()

# Display a message indicating that the plot has been saved
print("Plots saved to 'problem2_plots.png'")
