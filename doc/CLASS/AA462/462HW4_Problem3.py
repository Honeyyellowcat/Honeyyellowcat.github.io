import math

# Given data
p_c = 50 * 1.01325e5  # Chamber pressure in Pa
T_C = 3400  # Chamber temperature in K
gamma = 1.2  # Specific heat ratio
M = 15.5 * 1.66053904e-27  # Average molecular mass in kg
k = 0.1  # Thermal conductivity in W/m/K
mu = 1.27e-5  # Dynamic viscosity in kg/m/s
c_p = 3.23 * 1000  # Specific heat at constant pressure in J/kg/K

T_m = 2750  # Melting point in K
epsilon = 0.5  # Emissivity
D_t = 0.2  # Throat diameter in m

# Constants
R = 8.314  # Universal gas constant in J/mol/K
sigma = 5.67e-8  # Stefan-Boltzmann constant in W/m^2/K^4
T_inf = 300  # Ambient temperature in K

# Equations
R_specific = R / M  # Specific gas constant
a = math.sqrt(gamma * R_specific * T_C)  # Speed of sound 
rho_t = p_c / (R_specific * T_C)  # Density at the throat
mu_c = mu  # Dynamic viscosity at chamber
k_c = k  # Thermal conductivity at chamber
Re_t = rho_t * a * D_t / mu_c  # Reynolds number at the throat
Pr_t = c_p * mu_c / k_c  # Prandtl number at the throat

# Throat area
A_t = math.pi * (D_t / 2) ** 2

# Equations at Throat area
Mach_t = 1  # Mach number

# Equations
T_0 = T_C * (1 + (gamma - 1) / 2 * Mach_t ** 2)  # Stagnation temperature 
p_0 = p_c * (1 + (gamma - 1) / 2 * Mach_t ** 2) ** (gamma / (gamma - 1))  # Stagnation pressure 
mdot = rho_t * A_t * a  # Mass flow rate

# Usselt number using McAdams equation
Nu_t = 0.023 * Re_t ** (4 / 5) * Pr_t ** 0.3

# Convective heat transfer coefficient
h = Nu_t * k_c / D_t

# Surface area of the nozzle
A_s = math.pi * D_t

# Initial guess for surface temperature
T_s = T_0

# Define a function to calculate the radiative heat transfer rate
def calculate_radiative_heat_transfer(T_s):
    T_sur = T_inf
    Q_rad = epsilon * sigma * A_s * (T_s ** 4 - T_sur ** 4)
    return Q_rad

# Iterate to find the surface temperature where radiative heat transfer becomes significant
epsilon_threshold = 0.1  # Set a threshold for radiative heat transfer
max_iterations = 100
tolerance = 1e-6
for _ in range(max_iterations):
    # Calculate radiative heat transfer rate
    Q_rad = calculate_radiative_heat_transfer(T_s)
    
    # Check if radiative heat transfer becomes significant
    if Q_rad / mdot > epsilon_threshold:
        break
    
    # Update surface temperature for the next iteration
    T_s = (T_s + T_0) / 2  # Bisection method for convergence

# Calculate critical area ratio
A_Ae_critical = A_s / A_t

print("Critical Area Ratio for Passive Radiation Cooling:", A_Ae_critical)
