% Constants and parameters
pc = 50e5; % Chamber pressure in Pa
Tc = 3400; % Chamber temperature in Kelvin
gamma = 1.2; % Specific heat ratio
M = 15.5 * 1.66054e-27; % Average molecular mass in kg
k = 0.1; % Thermal conductivity in W/m/K
mu = 1.27e-4; % Dynamic viscosity in kg/m/s
cp = 3.23 * 1e3; % Specific heat at constant pressure in J/kg/K
Tm = 2750; % Melting point in Kelvin
epsilon = 0.5; % Emissivity
Dt = 0.2; % Throat diameter in meters

% Derived quantities
At = pi * (Dt/2)^2; % Throat area in m^2
Pr = mu * cp / k; % Prandtl number

% Mass flow rate
Ru = 8.314; % Universal gas constant in J/(mol*K)
mdot = pc * At / sqrt(gamma * Ru * Tc) * sqrt((gamma + 1)/2)^((gamma + 1)/(2*(gamma - 1)));

% Mach number range
Mach = linspace(0.1, 5, 100);

% Functions for nozzle area, temperature, and diameter
A = @(M) At * (M .* sqrt(1 + (gamma - 1)/2 * M.^2).^(2 * gamma / (gamma - 1)));
T = @(M) Tc * (1 + (gamma - 1)/2 * M.^2).^(-1);
D = @(M) 2 * sqrt(A(M) / pi);

% Reynolds number and convective heat transfer coefficient
Re = @(M) 4 * mdot ./ (mu * pi * D(M));
hg = @(M) 0.026 * k ./ D(M) .* (Re(M)).^(-0.8) .* (Pr).^(-0.4);

% Recovery temperature
Tr = @(M) T(M) .* (1 + (gamma - 1)/2 * Pr^(1/3) .* M.^2);

% Heat balance equation to find Mach number where passive cooling is possible
qout = @(M) epsilon * 5.67e-8 * Tr(M).^4; % Stefan-Boltzmann Law
qin = @(M) hg(M) .* (Tr(M) - Tm); % Convective heat transfer
f = @(M) hg(M) .* (Tr(M) - Tm) - epsilon * 5.67e-8 * Tm^4; % Equation to solve

% Print out Tr(M) and Tm for each Mach number
disp('Mach Number    Recovery Temperature    Melting Temperature');
disp('---------------------------------------------------------');
for M = Mach
    Tr_value = Tr(M);
    disp([num2str(M), '            ', num2str(Tr_value), '                    ', num2str(Tm)]);
end

Mmelt = fzero(f, 2); % Using fzero to find the root with an initial guess of 2

% Area ratio where passive cooling is achieved
epsilon_melt = A(Mmelt) / At;

% Plotting the graph
figure;
plot(Mach, epsilon * ones(size(Mach)), 'b--', 'LineWidth', 2); hold on;
plot(Mach, A(Mach) / At, 'r', 'LineWidth', 2);
xlabel('Mach Number');
ylabel('Area Ratio A/Ae');
title('Passive Cooling Switch');
legend('Switch Threshold', 'Area Ratio A/Ae');
grid on;

% Set x-axis limits to zoom in around the switch point
xlim([0, max(Mach)]);
hold off;


