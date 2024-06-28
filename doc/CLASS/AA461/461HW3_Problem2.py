# Constants
molecular_weight_propane = 44.1  # g/mol
molecular_weight_kerosene = 170  # g/mol
molar_mass_air = 28.97  # g/mol

# Stoichiometric combustion of propane
# C3H8 + 5 O2 -> 3 CO2 + 4 H2O
# Stoichiometric air/fuel ratio = (mass of air) / (mass of fuel)

# For propane
mass_air_per_mass_fuel_propane = 5 * 32 / (3 * 12 + 8)  # Mass air per mass fuel

# For kerosene (simulated jet fuel)
mass_air_per_mass_fuel_kerosene = 15 * 32 / (13 * 12 + 2 * 1)  # Mass air per mass fuel

# Air flow rate
air_flow_rate_kg_per_s = 40  # kg/s

# Stoichiometric combustion rate of fuel
stoichiometric_fuel_consumption_rate_kg_per_s_propane = air_flow_rate_kg_per_s / (1 + mass_air_per_mass_fuel_propane)
stoichiometric_fuel_consumption_rate_kg_per_hr_propane = stoichiometric_fuel_consumption_rate_kg_per_s_propane * 3600  # kg/hr

stoichiometric_fuel_consumption_rate_kg_per_s_kerosene = air_flow_rate_kg_per_s / (1 + mass_air_per_mass_fuel_kerosene)
stoichiometric_fuel_consumption_rate_kg_per_hr_kerosene = stoichiometric_fuel_consumption_rate_kg_per_s_kerosene * 3600  # kg/hr

# Fuel consumption rate for fuel-lean condition (phi = 0.6)
fuel_lean_consumption_rate_kg_per_s_propane = stoichiometric_fuel_consumption_rate_kg_per_s_propane * 0.6
fuel_lean_consumption_rate_kg_per_hr_propane = fuel_lean_consumption_rate_kg_per_s_propane * 3600  # kg/hr

fuel_lean_consumption_rate_kg_per_s_kerosene = stoichiometric_fuel_consumption_rate_kg_per_s_kerosene * 0.6
fuel_lean_consumption_rate_kg_per_hr_kerosene = fuel_lean_consumption_rate_kg_per_s_kerosene * 3600  # kg/hr

# Benefits of fuel-lean condition
benefits_fuel_lean = "Operating the engine at a fuel-lean condition can reduce emissions of pollutants such as CO and unburned hydrocarbons. However, it may increase the production of NOx compounds."
 
# Display results
print("Stoichiometric air/fuel ratio for propane:")
print("Mass air per mass fuel:", mass_air_per_mass_fuel_propane)
print("Stoichiometric fuel consumption rate (propane):")
print("kg/s:", stoichiometric_fuel_consumption_rate_kg_per_s_propane)
print("kg/hr:", stoichiometric_fuel_consumption_rate_kg_per_hr_propane)
print()
print("Stoichiometric air/fuel ratio for kerosene:")
print("Mass air per mass fuel:", mass_air_per_mass_fuel_kerosene)
print("Stoichiometric fuel consumption rate (kerosene):")
print("kg/s:", stoichiometric_fuel_consumption_rate_kg_per_s_kerosene)
print("kg/hr:", stoichiometric_fuel_consumption_rate_kg_per_hr_kerosene)
print()
print("Fuel consumption rate for fuel-lean condition (phi = 0.6):")
print("Propane:")
print("kg/s:", fuel_lean_consumption_rate_kg_per_s_propane)
print("kg/hr:", fuel_lean_consumption_rate_kg_per_hr_propane)
print("Kerosene:")
print("kg/s:", fuel_lean_consumption_rate_kg_per_s_kerosene)
print("kg/hr:", fuel_lean_consumption_rate_kg_per_hr_kerosene)
print()
print("Benefits of fuel-lean condition:", benefits_fuel_lean)
