import numpy as np
import matplotlib.pyplot as plt

# Constants
pc_pa = 100  # pc / pa
gammas = [1.2, 1.3, 1.4]  # Values of gamma

# Define the equation for cf
def calculate_cf(gamma, pe_pc):
    cf = (2 / gamma) * ((2 / (gamma + 1)) ** ((gamma + 1) / (gamma - 1))) * (1 - (pe_pc ** ((gamma - 1) / gamma)))
    return cf

# Expansion ratio values
epsilon_values = np.linspace(1, 10, 100)  # Adjust range according to your needs

# Plotting
plt.figure(figsize=(10, 6))

for gamma in gammas:
    cf_values = []
    for epsilon in epsilon_values:
        pe_pc = 1 / (1 + epsilon)  # Pe / Pc
        cf = calculate_cf(gamma, pe_pc)
        cf_values.append(cf)
    plt.plot(epsilon_values, cf_values, label=f'γ = {gamma}')

plt.title('Thrust Coefficient ($c_f$) vs Expansion Ratio ($\epsilon$)')
plt.xlabel('Expansion Ratio ($\epsilon$)')
plt.ylabel('Thrust Coefficient ($c_f$)')
plt.legend()
plt.grid(True)
plt.show()
