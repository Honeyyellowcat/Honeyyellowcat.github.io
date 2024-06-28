import math
import matplotlib.pyplot as plt


# TURBINE AND COMPRESSOR MATCHING chapter 8 402
# Compressor Parameters
T1 = 298  # Inlet total temperature in Kelvin
P1 = 101.3  # Inlet total pressure in kPa
alpha1 = 40  # Inlet angle in degrees
M1 = 0.5  # Mach number
diffusion_factor = 0.5
solidity = 1.0
rotor_chord_height_ratio = 0.5
stator_chord_height_ratio = 0.5
polytropic_efficiency_compressor = 0.9
stator_loss_coefficient = 0.03
gamma_compressor = 1.4
R_compressor = 0.287
mass_flow_rate = 60  # Mass flow rate in kg/s
rotor_angular_velocity = 1000  # Rotor angular velocity in rad/s

# Turbine Parameters
T_turbine_inlet = 298  # Combustor output
P_turbine_inlet = 101.3  # Combustor output
alpha1_turbine = 0  # Inlet angle in degrees for the first stage
M1_turbine = 0.4  # Mach number for the first stage
gamma_turbine = 1.3
R_turbine = 0.287
mean_radius = 0.25  # Mean radius in meters
mean_rotor_velocity = 250  # Mean rotor velocity in m/s

# Other Constants
Cp = 1005  # Specific heat at constant pressure for air in J/kg*K

# Turbine Design Parameters
# Adjusted based on the design
hub_tip_ratio = 0.034
degree_of_reaction = 0.5
stagnation_temperature_ratio = 1.0
work_ratio = 1.0
flow_coefficient = 0.5
stress_factor = 0.03

# Mass flow rate through the turbine stage
def calculate_mass_flow_rate():
    return mass_flow_rate

# Turbine work and pressure ratio
def calculate_work_and_pressure_ratio():
    U = mean_rotor_velocity
    a0 = math.sqrt(gamma_turbine * R_turbine * T_turbine_inlet)

    # Pressure ratio
    pressure_ratio = (1 - (U * (degree_of_reaction - 1) / (mean_radius * a0 * flow_coefficient))**2) ** (1 / (gamma_turbine - 1))

    # Work ratio
    work_ratio = (1 - pressure_ratio ** ((gamma_turbine - 1) / gamma_turbine)) / (1 - (T_turbine_inlet / stagnation_temperature_ratio))

    return work_ratio, pressure_ratio

# Turbine efficiency
def calculate_turbine_efficiency():
    _, pressure_ratio = calculate_work_and_pressure_ratio()
    total_temperature_ratio = (1 - pressure_ratio ** ((gamma_turbine - 1) / gamma_turbine))

    turbine_efficiency = total_temperature_ratio / (1 - (T_turbine_inlet / stagnation_temperature_ratio))

    return turbine_efficiency

# Determine if compressor bleed air is included in the design
def includes_compressor_bleed_air():
    # Placeholder function
    return False

# Define the number of turbine stages
num_stages = 5

# Function to calculate turbine efficiencies for each stage
def calculate_turbine_efficiencies():
    efficiencies = []
    for _ in range(num_stages):
        efficiency = calculate_turbine_efficiency()
        efficiencies.append(efficiency)
    return efficiencies

# Function to calculate pressure and temperature changes across all turbine stages
def calculate_pressure_temperature_changes():
    pressures = []
    temperatures = []
    for _ in range(num_stages):
        # Calculate pressure and temperature changes for each stage
        # This would involve your turbine design calculations
        # For demonstration purposes, let's assume some sample values
        pressure_change = 1.0
        temperature_change = 100.0
        pressures.append(pressure_change)
        temperatures.append(temperature_change)
    return pressures, temperatures

# Plot turbine efficiencies
efficiencies = calculate_turbine_efficiencies()
plt.figure(figsize=(8, 6))
plt.plot(range(1, num_stages + 1), efficiencies, marker='o', color='b')
plt.title('Turbine Efficiencies for Each Stage')
plt.xlabel('Turbine Stage')
plt.ylabel('Efficiency')
plt.grid(True)
plt.show()

# Plot pressure changes across turbine stages
pressures, temperatures = calculate_pressure_temperature_changes()
plt.figure(figsize=(8, 6))
plt.plot(range(1, num_stages + 1), pressures, marker='o', color='r')
plt.title('Pressure Changes Across Turbine Stages')
plt.xlabel('Turbine Stage')
plt.ylabel('Pressure Change')
plt.grid(True)
plt.show()

# Plot temperature changes across turbine stages
plt.figure(figsize=(8, 6))
plt.plot(range(1, num_stages + 1), temperatures, marker='o', color='g')
plt.title('Temperature Changes Across Turbine Stages')
plt.xlabel('Turbine Stage')
plt.ylabel('Temperature Change')
plt.grid(True)
plt.show()

# Main turbine considerations:
def calculate_turbine_considerations():
    mass_flow_rate = calculate_mass_flow_rate()
    work_ratio, pressure_ratio = calculate_work_and_pressure_ratio()
    turbine_efficiency = calculate_turbine_efficiency()
    compressor_bleed_air = includes_compressor_bleed_air()

    print("Turbine Considerations:")
    print("Mass Flow Rate:", mass_flow_rate, "kg/s")
    print("Work Ratio:", work_ratio)
    print("Pressure Ratio:", pressure_ratio)
    print("Turbine Efficiency:", turbine_efficiency)
    print("Includes Compressor Bleed Air:", compressor_bleed_air)

# Calculate turbine considerations:
calculate_turbine_considerations()
