import math

# Constants
chamber_pressure_atm = 100
inlet_fuel_temperature_K = 110
inlet_oxidizer_temperature_K = 90
throat_diameter_inch = 1
conical_half_angle_degrees = 15
expansion_ratio = 16
R_universal = 8.314462618  # J/(mol*K), Universal Gas Constant

# Ideal gas properties for CH4 and O2
molecular_mass_CH4 = 16.04  # g/mol
molecular_mass_O2 = 32.00  # g/mol
R_specific_CH4 = 8.314462618 / molecular_mass_CH4  # J/(g*K)
R_specific_O2 = 8.314462618 / molecular_mass_O2  # J/(g*K)

# Convert chamber pressure from atm to Pa
chamber_pressure_Pa = chamber_pressure_atm * 101325  # 1 atm = 101325 Pa

# Sea level operation parameters
sea_level_pressure_psi = 14.7  # psi
sea_level_pressure_Pa = sea_level_pressure_psi * 6894.76  # psi to pascal conversion

# Chamber temperature calculation using average of fuel and oxidizer temperatures
chamber_temperature_K = (inlet_fuel_temperature_K + inlet_oxidizer_temperature_K) / 2

# Average molecular mass of products
average_molecular_mass_amu = (molecular_mass_CH4 + molecular_mass_O2) / 2

# Ratio of specific heats of products
ratio_specific_heats_products = 1.25  # Assumed for hydrocarbon combustion products

# Calculate corrected values for conical nozzle
def corrected_values(conical_half_angle_degrees, expansion_ratio, gamma):
    # Corrections for conical nozzle
    correction_factor = (1 + (gamma + 1) / (2 * gamma) * (conical_half_angle_degrees * (math.pi / 180)) ** 2) ** (-gamma / (gamma - 1))
    expansion_ratio_corrected = expansion_ratio * correction_factor
    return expansion_ratio_corrected

expansion_ratio_corrected = corrected_values(conical_half_angle_degrees, expansion_ratio, ratio_specific_heats_products)

# Performance parameters
c_star = math.sqrt(R_universal * chamber_temperature_K / average_molecular_mass_amu) * 1000  # m/s, converting from m/s to m/s
F_v = chamber_pressure_Pa * throat_diameter_inch * 0.0254 * math.pi / 4  # Newtons
I_sp_v = c_star / 9.81  # s, specific impulse in seconds

# Calculate corrected values for c_f (nozzle exit velocity)
if expansion_ratio_corrected >= expansion_ratio:
    # Over-expanded nozzle
    c_f = math.sqrt((2 * ratio_specific_heats_products * R_universal * chamber_temperature_K) /
                    (ratio_specific_heats_products - 1) * (1 - (sea_level_pressure_Pa / chamber_pressure_Pa) **
                                                         ((ratio_specific_heats_products - 1) /
                                                          ratio_specific_heats_products)))  # m/s
elif expansion_ratio_corrected < expansion_ratio:
    # Under-expanded or optimally expanded nozzle
    c_f = math.sqrt((2 * ratio_specific_heats_products * R_universal * chamber_temperature_K) /
                    (ratio_specific_heats_products - 1) * (1 - (sea_level_pressure_Pa / chamber_pressure_Pa) **
                                                         ((ratio_specific_heats_products - 1) /
                                                          ratio_specific_heats_products)))  # m/s
else:
    # In case of no specific condition, set c_f as 0
    c_f = math.sqrt((2 * ratio_specific_heats_products * R_universal * chamber_temperature_K) /
                    (ratio_specific_heats_products - 1))  # m/s


# Nozzle Condition
if expansion_ratio_corrected < 1:
    nozzle_condition = "Under-expanded"
elif expansion_ratio_corrected > 1:
    nozzle_condition = "Over-expanded"
else:
    nozzle_condition = "Optimally expanded"

# Nozzle flow separation condition estimation
if expansion_ratio_corrected < 1:
    flow_separation = "Under-expanded flow may lead to separation"
elif expansion_ratio_corrected > 1.2:
    flow_separation = "Over-expanded flow may lead to separation"
else:
    flow_separation = "No separation expected"

# Sea level operation parameters
sea_level_pressure_psi = 14.7  # psi
sea_level_pressure_Pa = sea_level_pressure_psi * 6894.76  # psi to pascal conversion

# Sea level operation parameters
sea_level_F = F_v * (sea_level_pressure_Pa / chamber_pressure_Pa)
sea_level_I_sp = I_sp_v * (sea_level_pressure_Pa / chamber_pressure_Pa)

# Corrected sea level specific impulse and characteristic velocity
sea_level_I_sp_corrected = I_sp_v * (math.sqrt(chamber_temperature_K / inlet_fuel_temperature_K) * (1 + (ratio_specific_heats_products - 1) / 2) ** ((ratio_specific_heats_products + 1) / (2 * (ratio_specific_heats_products - 1))))
sea_level_c_f_v = c_f * (sea_level_pressure_Pa / chamber_pressure_Pa)

# Output
print("a) Chamber Temperature (Tc): {:.2f} K".format(chamber_temperature_K))
print("b) Average Molecular Mass of Products: {:.2f} amu".format(average_molecular_mass_amu))
print("c) Ratio of Specific Heats of Products: {:.2f}".format(ratio_specific_heats_products))
print("d) c_star: {:.2f} m/s".format(c_star))
print("   F_v: {:.2f} N".format(F_v))
print("   I_sp_v: {:.2f} s".format(I_sp_v))
print("   c_f: {:.2f} m/s".format(c_f))
print("e) Nozzle Condition: {}".format(nozzle_condition))
print("   Flow Separation: {}".format(flow_separation))

# Sea level operation output
print("f) Sea Level F: {:.2f} N".format(sea_level_F))
print("   Sea Level I_sp: {:.2f} s".format(sea_level_I_sp_corrected))
print("   Sea Level c_f: {:.2f} m/s".format(sea_level_c_f_v))
