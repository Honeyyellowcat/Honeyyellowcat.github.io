import sympy as sp

# Define symbols
a1, b1, a2, b2, r = sp.symbols('a1 b1 a2 b2 r')

# Part (a): Stage work independent of radius
# Stage work is the integral of rc_O from 0 to r
stage_work = sp.integrate(a1 * r**2 + b1, (r, 0, r))
# For stage work to be independent of radius, its derivative w.r.t. r must be zero
condition_a = sp.diff(stage_work, r)
print("Part (a): Condition for stage work independent of radius:", condition_a)

# Part (b): Degree of reaction independent of radius
# Degree of reaction is given by -a/r
# To keep it independent of radius, its derivative w.r.t. r must be zero
degree_of_reaction = -a2 / r
condition_b = sp.diff(degree_of_reaction, r)
print("Part (b): Condition for degree of reaction independent of radius:", condition_b)

# Part (c): Degree of reaction is 1/2 at all radii
# Condition for degree of reaction to be 1/2 at all radii
condition_c = -a1 / r + b1 + a2 / r + b2 - 1/2
print("Part (c): Condition for degree of reaction to be 1/2 at all radii:", condition_c)

# Part (d): Axial velocity distribution upstream of the rotor
# The axial velocity distribution is rc_O = a*r**2 + b
print("Part (d): Axial velocity distribution upstream of the rotor: rc_O = a*r**2 + b")


# Define symbols
b1, com, Um, r, rm, ratio = sp.symbols('b1 com Um r rm ratio')

# Part (e): Axial velocity distribution corresponding to case (c)
# The axial velocity distribution is given by b1 + com * Um * (r / rm) * (1 - ratio)
axial_velocity_case_c = b1 + com * Um * (r / rm) * (1 - ratio)
print("Part (e): Axial velocity distribution corresponding to case (c):", axial_velocity_case_c)