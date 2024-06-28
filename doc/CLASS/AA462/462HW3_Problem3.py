import numpy as np
import matplotlib.pyplot as plt

# Data provided by CEA (replace with actual CEA results)
phi_values = np.array([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5])  # Equivalence ratio

# Placeholder data (replace with actual CEA results)
T_c_values = np.array([3500, 3600, 3650, 3650, 3600, 3550, 3500, 3450, 3400])  # Chamber temperature (K)
M_values = np.array([2.8, 2.9, 3.0, 3.0, 2.9, 2.7, 2.5, 2.4, 2.3])  # Mach number
mol_mass_values = np.array([20, 20, 20, 20, 20, 20, 20, 20, 20])  # Molecular mass of products (amu)
char_velocity_values = np.array([1800, 1850, 1900, 1900, 1850, 1800, 1750, 1700, 1650])  # Char. velocity (m/s)
thrust_coeff_values = np.array([1.5, 1.6, 1.7, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2])  # Thrust coefficient
I_sp_values = np.array([330, 335, 340, 340, 335, 325, 310, 305, 300])  # Specific impulse (s)

# Convert m/s to s for I_sp
I_sp_values = I_sp_values / 9.81

# Plot T_c vs. phi
plt.figure()
plt.plot(phi_values, T_c_values, marker='o', linestyle='-', label='$T_c$')
plt.xlabel('Equivalence Ratio ($\phi$)')
plt.ylabel('Chamber Temperature ($T_c$ K)')
plt.title('Chamber Temperature vs. Equivalence Ratio')
plt.grid(True)
plt.legend()
plt.show()

# Plot M vs. phi
plt.figure()
plt.plot(phi_values, M_values, marker='o', linestyle='-', label='M')
plt.xlabel('Equivalence Ratio ($\phi$)')
plt.ylabel('Mach Number (M)')
plt.title('Mach Number vs. Equivalence Ratio')
plt.grid(True)
plt.legend()
plt.show()

# Plot I_sp vs. phi
plt.figure()
plt.plot(phi_values, I_sp_values, marker='o', linestyle='-', label='$I_{sp}$')
plt.xlabel('Equivalence Ratio ($\phi$)')
plt.ylabel('Specific Impulse ($I_{sp}$ s)')
plt.title('Specific Impulse vs. Equivalence Ratio')
plt.grid(True)
plt.legend()
plt.show()

# Create the table
print(f"{'Equivalence Ratio, 𝜑':<20}{'Chamber Temp., 𝑻𝒄 (K)':<20}{'Mol. Mass of Prod., 𝓜 (amu)':<20}{'Char. Velocity, 𝒄∗ (m/s)':<20}{'Thrust Coeff., 𝒄𝒇':<20}{'Specific Impulse, 𝑰𝒔𝒑 (s)':<20}")
for i in range(len(phi_values)):
    print(f"{phi_values[i]:<20}{T_c_values[i]:<20}{mol_mass_values[i]:<20}{char_velocity_values[i]:<20}{thrust_coeff_values[i]:<20}{I_sp_values[i]:<20}")
