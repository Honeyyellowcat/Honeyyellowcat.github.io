# Given data
T1 = 250  # Initial temperature of reactants in Kelvin

# Component data (moles, average specific heats, heat of formation)
components = [
    {"name": "C2", "moles": 0.1008, "C_pp": 36.3, "C_pt": 32.3, "h_f": 0},
    {"name": "H2", "moles": 0.3170, "C_pp": 32.9, "C_pt": 29.6, "h_f": 0},
    {"name": "O", "moles": 0.054, "C_pp": 20.9, "h_f": -245143},
    {"name": "H", "moles": 0.109, "C_pp": 20.9, "h_f": -216093},
    {"name": "OH", "moles": 0.233, "C_pp": 33.5, "h_f": -41870},
    {"name": "H2O", "moles": 1.512, "C_pp": 48.27, "h_f": 241827}
]

# Calculate change in enthalpy of combustion
delta_h_combustion = sum(component["moles"] * component["h_f"] for component in components)

# Calculate average molar specific heat of the products
# Here, we use only those components with known average specific heats
average_C_pp = sum(component["moles"] * component["C_pp"] for component in components if "C_pp" in component)

# Calculate flame temperature using the formula
flame_temperature = T1 + delta_h_combustion / average_C_pp

print("Delta h = {:.2f} kJ/kmol".format(delta_h_combustion))
print("Average C_pp = {:.3f} kJ/(kmol K)".format(average_C_pp))
print("Flame Temperature = {:.2f} K".format(flame_temperature))
