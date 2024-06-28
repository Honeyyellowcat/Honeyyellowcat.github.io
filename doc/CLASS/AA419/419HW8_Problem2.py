# Constants
sigma = 5.67e-8  # Stefan-Boltzmann constant in W m^-2 K^-4
surface_temperature_C = 37  # Surface temperature in Celsius
surface_area = 2  # Surface area in square meters
surrounding_temperature_C = 25  # Surrounding temperature in Celsius

# Convert temperatures to Kelvin
# Temperature Conversion from Celsius to Kelvin:
surface_temperature_K = surface_temperature_C + 273.15
surrounding_temperature_K = surrounding_temperature_C + 273.15

# Calculate radiative heat transfer rate
# Stefan-Boltzmann Law (Radiative Heat Transfer Rate):
radiative_heat_transfer_rate = sigma * surface_area * ((surface_temperature_K**4) - (surrounding_temperature_K**4))

# Average human metabolic rate
metabolic_rate = 100  # in Watts

# Print the results
print(f"Radiative heat transfer rate: {radiative_heat_transfer_rate:.2f} Watts")
print(f"Average human metabolic rate: {metabolic_rate} Watts")
