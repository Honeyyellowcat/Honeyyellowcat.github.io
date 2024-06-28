import math

# Given data
stage_ratios = [1.6, 1.4, 1.3]
adiabatic_efficiencies = [0.87, 0.89, 0.90]
gamma = 1.4  # Assuming air as the working fluid

# Calculate compressor pressure ratio (Pi_c) and overall adiabatic efficiency (eta_c)
Pi_c = math.prod([ratio for ratio in stage_ratios])
eta_c = math.prod([efficiency for efficiency in adiabatic_efficiencies])

# Calculate polytropic efficiency (n)
numerator = math.log(Pi_c)
denominator = sum([math.log(ratio**((gamma - 1)/gamma)) / efficiency for ratio, efficiency in zip(stage_ratios, adiabatic_efficiencies)])
polytropic_efficiency = numerator / denominator

# Calculate the difference between stage efficiency and polytropic efficiency
difference = [adiabatic_efficiency - polytropic_efficiency for adiabatic_efficiency in adiabatic_efficiencies]

# Display results
print(f"Compressor Pressure Ratio (Pi_c): {Pi_c:.4f}")
print(f"Overall Adiabatic Efficiency (eta_c): {eta_c:.4f}")
print(f"Average Polytropic Efficiency (n): {polytropic_efficiency:.4f}")
print(f"Difference between Stage Efficiency and Polytropic Efficiency: {difference}")
