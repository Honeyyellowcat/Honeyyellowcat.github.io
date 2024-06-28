import matplotlib.pyplot as plt
import numpy as np

def calculate_surface_temperatures(T_infinity_i, h_i, T_infinity_o, h_o, d):
    # Conversion factors
    h_i = 1 / h_i
    h_o = 1 / h_o

    # Steady-state heat transfer equation
    q_double_prime = (T_infinity_i - T_infinity_o) / (
        h_i + d / h_o
    )

    # Inner surface temperature
    T_sur_i = T_infinity_i - q_double_prime / h_i

    # Outer surface temperature
    T_sur_o = T_infinity_o + q_double_prime / h_o

    return T_sur_i, T_sur_o

# Given values for part (a)
T_infinity_i_a = 40  # °C
h_i_a = 30  # W/(m^2·K)
T_infinity_o_range = np.arange(-30, 1, 1)  # °C
d_a = 0.004  # m (thickness of the window glass)

# Values for h_o in part (b)
h_o_values = [2, 65, 100]  # W/(m^2·K)

# Plot for each h_o value
for h_o_val in h_o_values:
    T_sur_i_vals = []
    T_sur_o_vals = []

    for T_infinity_o_val in T_infinity_o_range:
        # Calculate surface temperatures for part (b)
        T_sur_i, T_sur_o = calculate_surface_temperatures(
            T_infinity_i_a, h_i_a, T_infinity_o_val, h_o_val, d_a
        )
        T_sur_i_vals.append(T_sur_i)
        T_sur_o_vals.append(T_sur_o)

    # Plot results
    plt.plot(T_infinity_o_range, T_sur_i_vals, label=f'h_o = {h_o_val} W/(m^2·K)')

plt.xlabel('$T_{\infty,o}$ (°C)')
plt.ylabel('Surface Temperature (°C)')
plt.title('Inner and Outer Surface Temperatures vs. $T_{\infty,o}$')
plt.legend()
plt.grid(True)
plt.show()
