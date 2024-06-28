import math

# Given data
gamma = 1.4
M2 = 0.5
Ma = 0.85

# Function to calculate Mach number from area ratio
def mach_from_area_ratio(A_ratio):
    mach = math.sqrt((2/(gamma - 1)) * ((1/A_ratio)**((gamma - 1)/gamma) - 1))
    return mach if mach != 0 else 1e-10  # Avoid division by zero, return a very small value if mach is zero

# Function to calculate area ratio using isentropic relation
def area_ratio_from_mach(M1, M2):
    A_ratio = (1/M1) * ((1 + (gamma - 1)/2 * M1**2) / (1 + (gamma - 1)/2 * M2**2))**((gamma + 1)/(2 * (gamma - 1)))
    return A_ratio

# Part (a) - Calculate M1 and A2/A1
# Inlet entrance Mach number, M1
M1 = 0.85  # Given flight Mach number
# Calculate Area ratio A2/A1
A2_A1 = 1 / ((1 / M1) * ((1 + (gamma - 1) / 2 * M1**2) / (1 + (gamma - 1) / 2 * M2**2))**((gamma + 1) / (2 * (gamma - 1))))

# Part (b) - Calculate A2/Aa
# Calculate A2/Aa
A2_Aa = area_ratio_from_mach(Ma, M2) # Using Ma as flight Mach number

# Output
print("Part (a):")
print("Inlet entrance Mach number, M1:", M1)
print("Area ratio A2/A1:", A2_A1)
print("\nPart (b):")
print("Area ratio A2/Aa:", A2_Aa)
print("\nPart (c):")
print("The spinner helps improve airflow distribution and reduces swirl effects.")
