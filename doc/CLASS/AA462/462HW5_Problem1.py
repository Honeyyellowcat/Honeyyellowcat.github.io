import numpy as np
import matplotlib.pyplot as plt

# Given parameters
rho_p = 1600  # kg/m^3
c_star = 1700  # m/s
c_f = 2
r_t = 0.02  # m
r_e = 0.10  # m
r_0 = 0.03  # m
r_f = 0.12  # m
I = 0.20  # m

# Constants
gamma = 1.2  # Assumption
n = 0.3  # Exponent for burn rate

# Time parameters
dt = 0.001  # Time step
t_max = 10.0  # Maximum time for simulation

# Initial conditions
w0 = r_0 - r_t  # Initial web distance
P_c_initial = 2.0  # MPa, initial chamber pressure

# Function to calculate burn rate
def burn_rate(P_c):
    return 0.4 * P_c ** 0.3

# Function to calculate area at any web distance w
def calculate_Ae(w):
    return np.pi * (r_e ** 2 - (r_e - w) ** 2)

# Function to calculate burn time
def calculate_burn_time(P_c_initial, dt):
    t = 0
    P_c = P_c_initial
    while P_c > 0 and t < t_max:
        P_c_dot = (rho_p * c_star * burn_rate(P_c) * calculate_Ae(w0)) / (2 * n * r_f * c_f) - (P_c / (rho_p * c_star))
        P_c += P_c_dot * dt
        t += dt
    return t

# Function to simulate web distance versus time
def simulate_web_distance(dt):
    t = np.arange(0, t_max, dt)
    w = np.zeros_like(t)
    P_c = P_c_initial
    for i in range(len(t)):
        if P_c <= 0:
            break
        w_dot = (2 * n * r_f * c_f * P_c) / (rho_p * c_star * burn_rate(P_c) * np.pi * r_e ** 2)
        w[i] = w0 + w_dot * t[i]
        P_c_dot = (rho_p * c_star * burn_rate(P_c) * calculate_Ae(w[i])) / (2 * n * r_f * c_f) - (P_c / (rho_p * c_star))
        P_c += P_c_dot * dt
    return t, w

# Function to calculate chamber pressure versus time
def calculate_chamber_pressure(t, w):
    P_c = np.zeros_like(t)
    P_c[0] = P_c_initial
    for i in range(1, len(t)):
        P_c_dot = (rho_p * c_star * burn_rate(P_c[i-1]) * calculate_Ae(w[i])) / (2 * n * r_f * c_f) - (P_c[i-1] / (rho_p * c_star))
        P_c[i] = P_c[i-1] + P_c_dot * dt
    return P_c

# Function to calculate thrust versus time
def calculate_thrust(P_c, w):
    thrust = np.zeros_like(P_c)
    for i in range(len(P_c)):
        Ae = calculate_Ae(w[i])
        thrust[i] = 2 * n * r_f * c_f * P_c[i] * Ae
    return thrust

# Main function to solve the problem
def main():
    # Part a) Calculate Ae as a function of w
    print("Part a) Equation for Ae as a function of w: Ae = pi * (r_e^2 - (r_e - w)^2)")
    
    # Part b) Simulate web distance versus time
    print("\nPart b) Simulating web distance versus time")
    t, w = simulate_web_distance(dt)
    print("Web distance versus time simulated successfully")
    
    # Part c) Calculate total burn time
    print("\nPart c) Calculating total burn time")
    total_burn_time = calculate_burn_time(P_c_initial, dt)
    print("Total burn time:", total_burn_time, "seconds")
    
    # Part d) Calculate chamber pressure versus time
    print("\nPart d) Calculating chamber pressure versus time")
    P_c = calculate_chamber_pressure(t, w)
    print("Chamber pressure versus time calculated successfully.")
    
    # Part e) Calculate thrust versus time
    print("\nPart e) Calculating thrust versus time")
    thrust = calculate_thrust(P_c, w)
    print("Thrust versus time calculated successfully")
    
    # Part f) Analyze thrust profile
    print("\nPart f) Analyzing thrust profile")
    if thrust[0] < thrust[-1]:
        thrust_profile = "progressive"
    elif thrust[0] > thrust[-1]:
        thrust_profile = "regressive"
    else:
        thrust_profile = "neutral"
    print("Thrust profile:", thrust_profile)
    
    # Plotting results
    plt.figure(figsize=(12, 8))
    
    # Part b) Web Distance versus Time
    plt.subplot(2, 2, 1)
    plt.plot(t, w)
    plt.title('Part b) Web Distance versus Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Web Distance (m)')
    
    # Part d) Chamber Pressure versus Time
    plt.subplot(2, 2, 2)
    plt.plot(t, P_c)
    plt.title('Part d) Chamber Pressure versus Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Chamber Pressure (MPa)')
    
    # Part e) Thrust versus Time
    plt.subplot(2, 2, 3)
    plt.plot(t, thrust)
    plt.title('Part e) Thrust versus Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Thrust (N)')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
