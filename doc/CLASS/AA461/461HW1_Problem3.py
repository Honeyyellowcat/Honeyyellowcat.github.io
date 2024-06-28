# Given values
T01 = 340  # Stagnation temperature at entrance to rotor in Kelvin
P01 = 185  # Stagnation pressure at entrance to rotor in kPa
Cu1 = 100  # Mid-radius velocity at entrance to rotor in m/s
Cu2 = 150  # Mid-radius velocity at exit of rotor in m/s

# Constants
c_p = 1000  # Specific heat at constant pressure in J/(kg*K) - replace with the actual value

# Part a: Specific work (kJ/kg)
T02 = T01 - (Cu2**2 - Cu1**2) / (2 * c_p)
w = c_p * (T01 - T02) / 1000  # Convert J to kJ

# Part b: Stagnation temperature between rotor and stator
T03 = T02

# Part c: Stagnation pressure between rotor and stator
P02 = P01  # Assuming no losses
P03 = P02

# Part d: Mid-radius pressure coefficient
rho = P01 / (287 * T01)  # Density calculation using ideal gas law
psi = (P02 - P03) / (0.5 * rho * (Cu1**2 - Cu2**2))

# Displaying the results
print(f"Part a: Specific work = {w:.2f} kJ/kg")
print(f"Part b: Stagnation temperature between rotor and stator (T03) = {T03:.2f} K")
print(f"Part c: Stagnation pressure between rotor and stator (P03) = {P03:.2f} kPa")
print(f"Part d: Mid-radius pressure coefficient (psi) = {psi:.4f}")
