import matplotlib.pyplot as plt
import numpy as np

# Constants
r1 = 1.0  # Inner radius
r2 = 2.0  # Outer radius
T1 = 100.0  # Temperature at inner surface
T2 = 50.0   # Temperature at outer surface

# Generate radii values
r_values = np.linspace(r1, r2, 100)

# Calculate corresponding temperature values using a concave function
T_values = T1 - (T1 - T2) * ((r_values - r1) / (r2 - r1))**2

# Plotting the T-r diagram
plt.plot(r_values, T_values)
plt.xlabel('Radius (r)')
plt.ylabel('Temperature (T)')
plt.title('Temperature Distribution in Insulation')
plt.grid(True)
plt.show()
