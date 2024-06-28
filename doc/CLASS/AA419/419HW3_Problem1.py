# Given parameters
H = 0.02  # Wall height in meters
w = 0.02  # Width of the wall in meters
t = 0.002  # Thickness of the wall in meters
L = 0.02  # Length of the wall in meters
Tb = 95 + 273.15  # Base temperature in Kelvin
T_infinity = 20 + 273.15  # Ambient temperature in Kelvin
h_max = 50  # Maximum convection heat transfer coefficient in W / (m^2 * K)
N_max = 10  # Maximum number of fins

# Function to calculate convection heat transfer coefficient
def calculate_heat_transfer_coefficient(N):
    return h_max * (1 - N / N_max)

# Function to calculate total heat rate
def calculate_heat_rate(h, A, delta_T):
    return h * A * delta_T

# Calculate surface area
A = 2 * (H * L + w * L) + N_max * t * L

# Calculate heat rate for different numbers of fins
for N in [0, 3, 6, 9]:
    # Calculate heat transfer coefficient
    h = calculate_heat_transfer_coefficient(N)
    
    # Calculate temperature difference
    delta_T = Tb - T_infinity
    
    # Calculate heat rate
    Q = calculate_heat_rate(h, A, delta_T)
    
    print(f"Total heat rate for {N} fins: {Q:.2f} Watts")
