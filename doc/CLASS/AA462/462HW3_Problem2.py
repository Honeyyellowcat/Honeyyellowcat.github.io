# Constants
R_universal = 8.314  # Universal gas constant in J/(mol*K)
R_universal_amu = 8.314 / (6.022e23)  # Universal gas constant in J/(mol*amu)

# Given data
Pc = 100 * 101325  # Chamber pressure in Pa
T_inlet = 298  # Inlet temperature in K
R = 50  # Nozzle expansion ratio

# Standard enthalpies of formation (in kJ/mol)
Hf_CH4 = -74.87
Hf_O2 = 0
Hf_CO2 = -393.51
Hf_H2O = -241.82

# Stoichiometric coefficients for the reaction
a = 1
b = 2

# Available heat of the reaction
Delta_H_rxn = (a * Hf_CO2 + b * Hf_H2O) - (Hf_CH4 + 2 * Hf_O2)  # in kJ/mol

# Convert heat of reaction to J/mol
Delta_H_rxn *= 1000

# Chamber temperature (Tc) calculation
Tc = T_inlet * (1 + (R_universal / (a * R_universal_amu)) * (Delta_H_rxn / (a * R_universal_amu * T_inlet)))

# Average molecular mass of the products
Molar_mass_CO2 = 44.01  # g/mol
Molar_mass_H2O = 18.02  # g/mol
molar_mass_avg = (a * Molar_mass_CO2 + b * Molar_mass_H2O) / (a + b)  # g/mol

# Vacuum specific impulse (Isp) calculation
Isp = (2 * R_universal * Tc) / (a * molar_mass_avg)

# Print the results
print("(i) Stoichiometric coefficients (a, b):", a, ",", b)
print("(ii) Available heat of the reaction (J/mol):", Delta_H_rxn)
print("(iii) Chamber temperature (K):", Tc)
print("(iv) Average molecular mass of the products (g/mol):", molar_mass_avg)
print("(v) Vacuum specific impulse (m/s):", Isp)
