import math

# Given data
M = 0.9  # Mach number at inlet
m_dot = 100  # Mass flow rate (kg/s)
A_inlet = 3.07  # Inlet area (m^2)
eta_diffuser = 0.9  # Adiabatic efficiency of the diffuser
M_2 = 0.4  # Mach number entering the compressor
T_ambient = 222  # Ambient temperature (K)
P_ambient = 9.57 * 1000  # Ambient pressure (Pa)
gamma = 1.4  # Specific heat ratio for air
R = 287  # Specific gas constant for air (J/(kg*K))

# Part (a): Inlet static pressure ratio to ambient pressure

# Speed of sound at the inlet
a_inlet = math.sqrt(gamma * R * T_ambient)

# Velocity at the inlet
V_inlet = M * a_inlet

# Inlet static temperature
T_inlet = T_ambient * (1 + (gamma - 1) / 2 * M**2)

# Inlet static pressure ratio to ambient pressure
P_inlet_to_ambient = (T_inlet / T_ambient)**(gamma / (gamma - 1))

# Part (b): Static pressure ratio across the internal diffuser

# Temperature at the exit of the diffuser
T_exit_diffuser = T_ambient * (1 + (gamma - 1) / 2 * M_2**2)

# Static pressure ratio across the diffuser
P_exit_to_inlet_diffuser = (T_exit_diffuser / T_inlet)**(gamma / (gamma - 1))

# Actual pressure ratio across the diffuser
P_exit_to_inlet_actual = 1 + eta_diffuser * (P_exit_to_inlet_diffuser - 1)

# Part (c): Fraction of inlet dynamic pressure converted to static pressure

# Inlet static pressure
P_inlet = P_ambient * P_inlet_to_ambient

# Density at the inlet
rho_inlet = P_inlet / (R * T_inlet)

# Inlet dynamic pressure
P_dynamic_inlet = 0.5 * rho_inlet * V_inlet**2

# Fraction of inlet dynamic pressure converted to static pressure
fraction_dynamic_to_static = (P_inlet - P_ambient) / P_dynamic_inlet

# Output results
print("Part (a): Inlet static pressure ratio to ambient pressure:", P_inlet_to_ambient)
print("Part (b): Static pressure ratio across the internal diffuser:", P_exit_to_inlet_actual)
print("Part (c): Fraction of inlet dynamic pressure converted to static pressure:", fraction_dynamic_to_static)

