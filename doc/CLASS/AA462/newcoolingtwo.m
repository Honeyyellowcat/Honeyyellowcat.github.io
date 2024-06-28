clc
clear
close all

% Parameters
De = 0.05; % Diameter of the tube (m)
tw = 0.005; % Thickness of the tube wall (m)
m_f = 11.742; % Mass flow rate of the fuel (kg/s) From Table
Pli = 303.98; % Initial pressure (Bar) From Table
Tli = 855.71; % Initial  temperature (K) From Table
V = 2305.6; % Velocity (m/s) From Table

% At 2878.64 Properties for liquid hydrogen (H2) and liquid oxygen (O2)
rho_l_hydrogen = 67.85; % at 20k - Density of liquid hydrogen at given Temp (kg/m^3)
rho_l_oxygen = 1080; % Density of liquid oxygen at given Temp (kg/m^3)
mu_l_hydrogen = 1.14e-5; % Dynamic viscosity of liquid hydrogen (kg/(m*s))
mu_l_oxygen = 2.1e-5; % Dynamic viscosity of liquid oxygen (kg/(m*s))
Pr = 1.28; % Prandtl number

% Integration parameters
dx = 0.01; % Incremental length (m)
x_final = 1.0; % Final length of the tube (m)

% Calculate Reynolds number pg 203 and eq 6.25
Re = (rho_l_hydrogen + rho_l_oxygen) * V * De / (mu_l_hydrogen + mu_l_oxygen);

% Calculate thermal conductivity
k = 0.026 * Re^0.8 * Pr^0.4;

% Friction coefficient based on Reynolds number. Moody diagram pg 209
% eq  6.37
if Re < 2100
    cf = 16 / Re; % Laminar flow
elseif Re >= 2100 && Re < 5000
    cf = 0.046 / Re^0.2;
elseif Re >= 5000 && Re < 200000
    cf = 0.0014 + 0.125 / Re^0.32;
else
    cf = 0; % Default value
end   

% Step 2: Calculate N and m_chan pg 206 eq 6.30 and 6.31
N = pi * (De + 0.8 * (De + 2 * tw)) / (De + 2 * tw);
m_chan = m_f / N;

% Step 4: Guess the wall temperature on the gas side, Twgi (initial guess)
Twgi = 2; % Initial guess for the gas temperature on the wall (K)

% Step 5: hg then q pg 195
hg = 1; % Example value for convective heat transfer coefficient (W/m^2*K)
Tr = 5; % Example gas temperature (K)
q = hg * (Tr - Twgi); % Heat flux (W/m^2)

% Step 6: Twli from conduction through the wall
k_stainless_steel = 16.3; % Thermal conductivity of stainless steel (W/m*K)
Twli = Twgi - q * tw / k_stainless_steel;

% Step 7: hl based on Tl(i-1)
Tl_prev = Tli; % Example initial temperature
hl = 200; % Example value for convective heat transfer coefficient (W/m^2*K)

% Step 8: Heat flux pg 204 eq 6.29
q = hl * (Twli - Tl_prev); % (W/m^2)

% Step 10: Obtain new liquid temperature in the ith segment
% (Assuming heat dumped in over the incremental length delta x)
bi = De * pi; % Circumferential span of the channel (m)
Tl_new = Tl_prev + (q * bi * x_final) / (m_chan * pi * De^2 / 4 * V^2); 

% New liquid pressure
Pl_new = Pli - 4 * cf * x_final / De^2 * (rho_l_hydrogen + rho_l_oxygen) * V^2 / 2; 

% Final results
%disp(['Number of tubes: ' num2str(N)])
%disp(['Mass flow Rate (m_chan): ' num2str(m_chan) ' kg/s'])
%disp(['Heat flux (q) ' num2str(q) ' W/m^2'])
disp(['Final liquid temp: ' num2str(Tl_new) ' K']);
disp(['Final liquid pressure: ' num2str(Pl_new) ' Bar']); 
