% Constants
gamma = 1.25; % Specific heat ratio
R = 8.314; % Gas constant (J/(mol*K))
Pr = 0.7; % Prandtl number (for air)
mu = 1.5e-5; % Dynamic viscosity of air (kg/(m*s))
k_g = 0.05; % Thermal conductivity of gases (W/(m*K))
Cp_coolant = 14e3; % Specific heat capacity of coolant (J/(kg*K))
m_dot_coolant = 5; % Coolant mass flow rate (kg/s)
T_inlet = 100; % Coolant inlet temperature (K)
T_limit = 300; % Coolant outlet temperature limit (K)
Dt = 0.15; % Nozzle throat diameter (m)
L = 1; % Nozzle length (m)
Dc = 5e-3; % Coolant channel diameter (m)
N_channels = 100; % Number of coolant channels
T_c = 3500; % Chamber temperature (K)

% Calculations
At = pi*(Dt/2)^2; % Throat area (m^2)
m_dot_gas = 100; % Assume a value for the mass flow rate of gases (kg/s)

% Specific heat capacity of gases (using specific heat ratio gamma)
Cp_g = R / (gamma - 1); % J/(kg*K)

% Reynolds number for coolant flow
Re = 4 * m_dot_coolant / (pi * Dc * mu);

% Convective heat transfer coefficient for coolant flow
hc = 0.023 * Re^0.8 * (Pr^(1/3)) * (mu/Dc); % Using Dittus-Boelter equation

% Calculate heat transfer rate from gases to nozzle material (assuming steady-state)
Q_transfer = m_dot_gas * Cp_g * (T_c - T_inlet); % Joules per second

% Calculate temperature rise of coolant
Q_coolant = Q_transfer / (m_dot_coolant * Cp_coolant); % Temperature rise of coolant (K)

% Check if coolant temperature rise exceeds limit
if Q_coolant > (T_limit - T_inlet)
    disp('Coolant outlet temperature exceeds limit!');
else
    disp('Coolant outlet temperature within limit.');
end

% Calculate pressure drop across coolant channels (assuming turbulent flow)
deltaP = 4 * m_dot_coolant * hc * L / (pi * Dc^2 * N_channels);

% Display results
disp(['Reynolds number for coolant flow: ', num2str(Re)]);
disp(['Convective heat transfer coefficient for coolant flow: ', num2str(hc), ' W/(m^2*K)']);
disp(['Temperature rise of coolant: ', num2str(Q_coolant), ' K']);
disp(['Pressure drop across coolant channels: ', num2str(deltaP), ' Pa']);
