clc
clear
close all

% Given parameters
pc = 50 * 1.01325e5; % Chamber pressure in Pa
Tc = 3400; % Chamber temperature in Kelvin
gamma = 1.2; % Specific heat ratio
M = 15.5 * 1.66053904e-27; % Average molecular mass in kg
k = 400; % Thermal conductivity of copper in W/m/K (just an example value, please adjust as per actual copper properties)
mu = 1.27e-4; % Dynamic viscosity in kg/m/s
cp = 385; % Specific heat at constant pressure for copper in J/kg/K (just an example value, please adjust as per actual copper properties)
Tm = 1358; % Melting point of copper in Kelvin
epsilon = 0.5; % Emissivity (adjust as needed)
Dt = 0.2; % Throat diameter in meters
desired_epsilon = 0.8; % Desired emissivity for cooling (adjust as needed)

% Calculations
At = pi * (Dt/2)^2; % Throat area in square meters
Pr = mu * cp / k; % Prandtl number for copper
m_dot = pc * At / sqrt(gamma * M / (8.314 * Tc) * (2/(gamma+1))^((gamma+1)/(gamma-1))); % Mass flow rate in kg/s

disp(['Throat Area (At): ', num2str(At), ' m^2']);
disp(['Prandtl Number (Pr): ', num2str(Pr)]);
disp(['Mass Flow Rate (m_dot): ', num2str(m_dot), ' kg/s']);

% Function to calculate area, temperature, and diameter as functions of Mach number
A = @(M) At * ((1 + (gamma-1)/2 * M^2) / ((gamma+1)/2)^(gamma/(gamma-1)));
T = @(M) Tc * (1 + (gamma - 1)/2 * M^2)^(-1);
D = @(M) 2 * sqrt(At * ((1 + (gamma-1)/2 * M^2) / ((gamma+1)/2)^(gamma/(gamma-1))) / pi);

% Function to calculate Reynolds number
Re = @(M) 4 * m_dot / (mu * pi * D(M));

% Function to calculate convective heat transfer coefficient
hg = @(M) 0.026 * k / D(M) * (Re(M))^0.8 * (Pr)^0.4;

% Function to calculate recovery temperature
Tr = @(M) T(M) * (1 + (gamma - 1)/2 * (Pr)^(1/3) * M^2);

% Function to calculate heat balance equation
Mmelt = fzero(@(M) hg(M) * (Tr(M) - Tm) - epsilon * 5.67e-8 * (Tr(M))^4, 2.73);

% Calculate the area ratio where passive cooling is possible
epsilon_melt = A(Mmelt) / At;

disp(['Mach Number at which passive cooling becomes possible (Mmelt): ', num2str(Mmelt)]);
disp(['Emissivity at which passive cooling becomes possible (epsilon_melt): ', num2str(epsilon_melt)]);

% Finding the Mach number corresponding to desired emissivity
M_desired = fzero(@(M) A(M) / At - desired_epsilon, 2.0);

disp(['The Mach number at which desired emissivity is achieved (M_desired): ', num2str(M_desired)]);

