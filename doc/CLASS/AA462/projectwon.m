clc
clear
close all

%% Heat transfer 
hg = 10; % Heat transfer coefficient from gas to wall (W/m^2*K)
Tr = 120; % Temperature of gas (in Kelvin)
Twg = 100; % Temperature of gas at the wall (in Kelvin)
k = 385; % Thermal conductivity of copper (W/m*K) - Updated for copper
Twl = 800; % Temperature of wall at the fluid side (in Kelvin)
hl = 20; % Heat transfer coefficient from wall to fluid (W/m^2*K)
Tl = 300; % Temperature of fluid (in Kelvin)

% Heat transfer
q = hg * (Tr - Twg); % Heat transfer rate from gas to wall
disp(['Heat transfer rate (q): ', num2str(q)]);

%% Tube/Channel Design 
Dt = 0.05; % Throat diameter (m)
De = 0.1; % Outer diameter of the tube (m)
d = 0.08; % Inner diameter of the tube (m)
tw = 0.005; % Wall thickness of the tube (m)
N = 10; % Total number of tubes/channels

% Number of tubes
N = pi * (De + 0.8 * (d + 2 * tw)) / (d + 2 * tw);
disp(['Tube/Channel Design: Number of tubes (N): ', num2str(N)]);

%% Structural Integrity 
E = 110e9; % Young's modulus of copper (Pa) - Updated for copper
Ec = 220e6; % Critical buckling stress of copper (Pa) - Updated for copper
nu = 0.34; % Poisson's ratio for copper

% Tangential stress
pl = 20e6; % Pressure of H2 fuel (Pa)
pg = 20e6; % Pressure of O2 oxidizer (Pa)
D = 0.1; % Outer diameter of the tube (m)
w = 0.02; % Width (m)
q_t_w = 5; % Heat flux (W/m^2)
sigma_t = ((pl * pg) * D / (2 * tw)) * (w / tw)^2 + (E * q_t_w) / (2 * (1 - nu) * k);
disp(['Structural Integrity: Tangential stress (sigma_t): ', num2str(sigma_t)]);

% Longitudinal stress
Thot = 500; % Hot temperature (K)
Tcold = 300; % Cold temperature (K)
delta_T = Thot - Tcold;
Ea = 1e-5; % Coefficient of thermal expansion
sigma_1 = Ea * delta_T;
disp(['Structural Integrity: Longitudinal stress (sigma_1): ', num2str(sigma_1)]);

% Buckling stress
sigma_b = E * Ec * (tw / D) * sqrt(abs(E - Ec))^2 / sqrt(3 * (1 - nu^2));
disp(['Structural Integrity: Buckling stress (sigma_b): ', num2str(sigma_b)]);

%% Pressure drop along the coolant passages
d = 0.01; % Local hydraulic diameter of the coolant passage (m)
rho_l = 1000; % Density of the coolant (kg/m^3)
V = 10; % Velocity of the coolant (m/s)
Re = 50000; % Reynolds number

% Relative roughness 
epsilon_d = 0.0002; 

% Friction factor calculation based on Moody diagram (Book pg 209)
if Re < 2100
    cf = 16 / Re; % Laminar flow
elseif Re >= 5000 && Re <= 200000
    cf = 0.046 / Re^0.2;
elseif Re > 3000 && Re <= 3e6
    cf = 0.0014 + 0.125 / Re^0.32;
else
    disp('Reynolds number out of range');
    return;
end

% Pressure drop 
delta_p = 4 * cf * rho_l * V^2 * (d);
% Display results
disp(['Pressure drop: Friction factor (cf): ', num2str(cf)]);
disp(['Pressure drop: Pressure drop (delta_p): ', num2str(delta_p)]);

% Switching criteria
switching_criteria_met = false;

% Thresholds for switching
heat_transfer_threshold = 500; % Make sure its a appropriate threshold
pressure_drop_threshold = 1000; % Make sure its a appropriate threshold
stress_threshold = 20000; % Make sure its a appropriate threshold

% Check if any of the criteria exceed the thresholds
if q < heat_transfer_threshold || delta_p > pressure_drop_threshold || sigma_t > stress_threshold || sigma_1 > stress_threshold || sigma_b > stress_threshold
    switching_criteria_met = true;
end

%% Implement switching 
if switching_criteria_met
    disp('Switching from active to passive cooling.');
else
    disp('Active cooling continues.');
end
% Print the value of switching_criteria_met
disp(['Switching criteria met: ', num2str(switching_criteria_met)])