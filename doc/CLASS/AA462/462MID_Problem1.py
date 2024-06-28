import numpy as np
import matplotlib.pyplot as plt

# Given parameters
delta_v = 8000  # m/s
I_sp = 350      # s
m_p = 4000      # kg
sigma = 0.15    # stage structural factor
sigma_prime = sigma
P = 1000        # $/kg
g_0 = 9.81      # m/s^2

# Calculate effective exhaust velocity
v_e = I_sp * g_0

# Define the function to calculate C
def calculate_C(m1, m2):
    beta_1 = np.exp(-delta_v / v_e)
    beta_2 = np.exp(-(delta_v / v_e) * (m1 / m2))
    N1 = np.log(1 / (1 - beta_1)) / sigma
    N2 = np.log(1 / (1 - beta_2)) / sigma_prime
    m0 = (m1 + m_p) / (1 - beta_1 / N1 - beta_2)
    C = P * m0
    return C

# Define range of m1 values
m1_values = np.linspace(1, 10, 100)

# Calculate C for each m1 value with m2 = 5
C_values = [calculate_C(m1, 5) for m1 in m1_values]

# Plot C vs. m1
plt.plot(m1_values, C_values)
plt.xlabel('m1')
plt.ylabel('Cost (C)')
plt.title('Cost vs. m1 for m2 = 5')
plt.grid(True)
plt.show()
