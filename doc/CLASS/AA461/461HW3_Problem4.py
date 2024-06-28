import numpy as np
from scipy.optimize import fsolve

# Constants
R = 8.314  # Ideal gas constant, J/(mol*K)

# Molar masses of elements (in g/mol)
M_C = 12.01
M_H = 1.008
M_O = 16.00
M_N = 14.01

# Given compositions
phi = 1.0  # Equivalence ratio
T_initial = 298  # Initial temperature, K
P = 1  # Pressure, atm

# Molar fractions of elements in air
X_O2 = 0.21
X_N2 = 0.79

# Molar masses of molecules (in g/mol)
M_propane = 3 * M_C + 8 * M_H
M_O2 = 2 * M_O
M_N2 = 2 * M_N

# Stoichiometric coefficients
coeff_C3H8 = 1
coeff_O2 = 5  # From the balanced equation
coeff_CO2 = 3
coeff_H2O = 4
coeff_CO = 0  # In case ii)
coeff_N2 = 5

# Enthalpies of formation (in kJ/mol) at 298 K
Hf_C3H8 = -103.85
Hf_O2 = 0
Hf_N2 = 0
Hf_CO2 = -393.51
Hf_H2O = -241.82
Hf_CO = -110.53  # In case ii)

# Enthalpy of reaction (in kJ/mol)
def enthalpy_of_reaction(T):
    H_reactants = coeff_C3H8 * Hf_C3H8 + coeff_O2 * Hf_O2 + coeff_N2 * Hf_N2
    H_products = coeff_CO2 * Hf_CO2 + coeff_H2O * Hf_H2O + coeff_CO * Hf_CO + coeff_N2 * Hf_N2
    return H_products - H_reactants

# Energy balance equation
def energy_balance(T):
    return enthalpy_of_reaction(T) - R * T_initial + R * T - 0

# Solving for adiabatic flame temperature
T_ad = fsolve(energy_balance, T_initial)

print("Adiabatic flame temperature:", T_ad[0], "K")
