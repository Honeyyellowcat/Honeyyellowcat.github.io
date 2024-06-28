import matplotlib.pyplot as plt

# Define the pressure values (in PSIA) and corresponding performance parameters
pressure_values = [5.9, 7.4, 8.8, 10.3, 11.8, 13.2, 14.7]  # PSIA
adiabatic_flame_temperature = [300.000, 300.000, 300.000, 300.000, 300.000, 300.000, 300.000]  # K (Placeholder values)
thrust_coefficient = [0.7145, 0.7145, 0.7145, 0.7145, 0.7145, 0.7145, 0.7145]  # Placeholder values
specific_impulse = [420.9, 420.9, 420.9, 420.9, 420.9, 420.9, 420.9]  # Placeholder values

# Plot adiabatic flame temperature vs. pressure
plt.figure(figsize=(10, 6))
plt.plot(pressure_values, adiabatic_flame_temperature, marker='o', color='blue')
plt.xlabel('Pressure (PSIA)')
plt.ylabel('Adiabatic Flame Temperature (K)')
plt.title('Adiabatic Flame Temperature vs. Pressure')
plt.grid(True)
plt.show()

# Plot thrust coefficient vs. pressure
plt.figure(figsize=(10, 6))
plt.plot(pressure_values, thrust_coefficient, marker='o', color='green')
plt.xlabel('Pressure (PSIA)')
plt.ylabel('Thrust Coefficient (Cf)')
plt.title('Thrust Coefficient vs. Pressure')
plt.grid(True)
plt.show()

# Plot specific impulse vs. pressure
plt.figure(figsize=(10, 6))
plt.plot(pressure_values, specific_impulse, marker='o', color='red')
plt.xlabel('Pressure (PSIA)')
plt.ylabel('Specific Impulse (Isp) (m/s)')
plt.title('Specific Impulse vs. Pressure')
plt.grid(True)
plt.show()
