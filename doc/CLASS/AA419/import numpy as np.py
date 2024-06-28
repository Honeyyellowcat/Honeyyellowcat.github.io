import numpy as np

# Constants and parameters
alpha = 0.21 / (1990 * 1470)  # thermal diffusivity
L = 0.005  # thickness in meters
T_soft = 363.15  # softening temperature in Kelvin
T_h = 573.15  # hot temperature in Kelvin
T_i = 293.15  # initial temperature in Kelvin
epsilon = 1e-6  # tolerance for convergence
N = 1000  # number of terms in the series

# Function to compute the sum
def compute_sum(t):
    total = 0
    for n in range(1, N+1):
        total += (1 - (-1)**n) / (n**2) * np.exp(-alpha * ((n * np.pi / L)**2) * t)
    return total

# Initial guess for t
t = 0

# Initial values for the sum
S_prev = 0
S_current = compute_sum(t)

# Iterative approximation
while np.abs(S_current - S_prev) >= epsilon:
    S_prev = S_current
    t += 0.001  # step size for iteration
    S_current = compute_sum(t)

# Output the result
print("Time for the back side to reach softening temperature:", round(t, 2), "seconds")
