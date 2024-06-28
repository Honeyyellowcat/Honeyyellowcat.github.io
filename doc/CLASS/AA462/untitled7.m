clc
clear
close all
% Problem data
pc = 50 * 1.01325e5; % Chamber pressure in Pa
Tc = 3400; % Chamber temperature in Kelvin
gamma = 1.2; % Specific heat ratio
M = 15.5 * 1.66054e-27; % Average molecular mass in kg
k = 0.1; % Thermal conductivity in W/m/K
mu = 1.27e-4; % Dynamic viscosity in kg/(m*s)
cp = 3.23 * 1e3; % Specific heat at constant pressure in J/kg/K
Tm = 2750; % Melting point in Kelvin
epsilon = 0.5; % Emissivity
Dt = 0.2; % Throat diameter in meters

% Calculations
At = pi * (Dt / 2)^2; % Throat area in square meters
Ru = 8.314; % Universal gas constant in J/(mol*K)
m_dot = pc * At * sqrt(gamma / (Ru * Tc) * ((2 / (gamma + 1))^((gamma + 1) / (gamma - 1)))); % Mass flow rate in kg/s

% Functions
A = @(M) (At ./ M) .* ((2 + (gamma - 1) * M.^2) ./ (gamma + 1)).^((gamma + 1) ./ (2 * (gamma - 1)));
T = @(M) Tc * (1 + (gamma - 1) / 2 * M.^2).^-1;
D = @(M) sqrt(A(M) ./ pi);

% McAdams Pipe Flow scaling laws
Re = @(M) (4 .* m_dot) ./ (mu * pi * D(M));
Pr = cp * mu / k;
hg = @(M) 0.026 * k ./ D(M) .* (Re(M).^0.8) .* (Pr.^0.4);

% Recovery temperature function
Tr = @(M) T(M) .* (1 + (gamma - 1) / 2 * (Pr.^(-1/3)) .* M.^2);

% Solve for Mmelt using the heat balance equation
options = optimset('Display','off');
Mmelt = fzero(@(M) hg(M) .* (Tr(M) - Tm) - epsilon * 5.67e-8 * (Tr(M).^4 - Tm^4), 2.73, options);

% Calculate the area ratio
epsilon_melt = A(Mmelt) / At;

% Display results
disp(['Throat Area (At): ', num2str(At), ' square meters']);
disp(['Mass Flow Rate (m_dot): ', num2str(m_dot), ' kg/s']);
disp(['Recovery Temperature (Tr): ', num2str(Tr(Mmelt)), ' K']);
disp(['Area Ratio for Passive Cooling (A/Ae): ', num2str(epsilon_melt)]);
