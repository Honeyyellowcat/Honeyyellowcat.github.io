import math

# Constants
Pr = 0.7  # Prandtl number
Re_x = 5e5  # Reynolds number at position x

# Calculate local Nusselt number at position x
Nu_x = 0.664 * Re_x**0.5 * Pr**(1/3)

# Calculate average Nusselt number from leading edge to position x
# For laminar flow over a flat plate, it's known that average Nu_x = 0.664 * Re_x**(1/2) * Pr**(1/3)
average_Nu_x = 0.664 * Re_x**(1/2) * Pr**(1/3)

# Calculate the ratio of average heat transfer coefficient to the local heat transfer coefficient
ratio = average_Nu_x / Nu_x

print("Ratio of the average heat transfer coefficient to the local heat transfer coefficient:", ratio)
