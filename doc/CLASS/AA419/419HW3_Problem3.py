# Given data
T_inlet = 250  # Inlet temperature in K

# Component data: [moles, Cp_p_bar, Cp_t_bar, H_f_bar]
components = {
    'C2': [0.1008, 36.3, 32.3, 0],
    'H2': [0.3170, 32.9, 29.6, 0],
    'O': [0.054, 20.9, None, 245143],
    'H': [0.109, 20.9, None, 216093],
    'OH': [0.233, 33.5, None, 41870],
    'H2O': [1.512, 48.27, None, -241827]
}

# Constants
R_universal = 8.314  # Universal gas constant in J/(mol*K)

# Function to calculate average specific heat
def average_specific_heat(Cp_p_bar, Cp_t_bar, T_flame):
    if Cp_t_bar is None:
        return Cp_p_bar  # If Cp_t_bar is None, use Cp_p_bar
    else:
        return (Cp_p_bar + Cp_t_bar) / 2


# Function to calculate enthalpy change
def enthalpy_change(moles, H_f_bar):
    return moles * H_f_bar

# Initial guess for flame temperature
T_flame_guess = 3000  # Initial guess in K

# Tolerance for convergence
tolerance = 1e-6

# Iterative calculation of flame temperature using energy balance
while True:
    Cp_sum = 0
    H_sum = 0
    for component, data in components.items():
        moles, Cp_p_bar, Cp_t_bar, H_f_bar = data
        Cp_avg = average_specific_heat(Cp_p_bar, Cp_t_bar, T_flame_guess)
        Cp_sum += moles * Cp_avg
        H_sum += enthalpy_change(moles, H_f_bar)
    
    # Energy balance equation
    T_flame_new = T_inlet + (H_sum / Cp_sum)
    
    # Check for convergence
    if abs(T_flame_new - T_flame_guess) < tolerance:
        break
    
    # Update guess for next iteration
    T_flame_guess = T_flame_new

# Output the result
print("Flame Temperature:", T_flame_new, "K")
