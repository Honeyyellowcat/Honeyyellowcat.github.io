clc
clear
close all
%Pg 211
% Regenerative Cooling System Analysis

% Define system parameters and initial conditions
% You will need to specify the values for these parameters
% based on your specific system design.

% Constants and properties
De = 0.1; % Diameter of the tube/channel (m)
tw = 0.005; % Thickness of the wall (m)
d = 0.15; % Width of the channel (m)
m_f = 0.1; % Mass flow rate of the coolant (kg/s)
Tr = 1000; % Gas temperature (K)
Ea = 1.5e11; % Young's modulus of the material (Pa)
k = 50; % Thermal conductivity of the wall material (W/(m*K))
v_v = 0.3; % Poisson's ratio
w = 0.02; % Internal width of the channel (m)
Tcold = 300; % Cold temperature in the tubes (K)
Thot = 1500; % Hot temperature in the tubes (K)

% Other variables
pl1 = 100000; % Initial pressure of the liquid (Pa)
Tl1 = 300; % Initial temperature of the liquid (K)
x_length = 10; % Length of the passage (m)
delta_x = 0.1; % Incremental length (m)
cfi = 1.0; % Example value for coefficient cfi
rho_l = 10;
l = 10;
v = 10;
pg=10;
Ec=10;


% Integration loop
i = 1;
x = 0;
while x < x_length
    % Step 2: Calculate N and m_chan
    N = pi*(De + 0.8*(d + 2*tw))/(d + 2*tw);
    m_chan = m_f/N;
    
    % Step 4: Guess Twgi
    Twgi = 500; % Example value, initial guess for Twgi
    
    % Step 5: Calculate hg and q
    % You need to calculate hg using correlations based on your system
    hg = 100; % Example value, to be calculated using correlations
    q = hg * (Tr - Twgi);
    
    % Step 6: Calculate Twli
    Twli = Twgi - q*tw/k;
    
    % Step 7: Compute hl
    % You need to compute hl based on Tl(i-1)
    hl = 50; % Example value, to be calculated based on Tl(i-1)
    
    % Step 8: Compute heat flux q
    q = hl*(Twli - Tl1);
    
    % Step 10: Compute new liquid temperature
    % You need to compute new liquid temperature based on heat dumped
    % into the incremental length Δx
    Pli = pl1 * cfi * delta_x / d^2 / (2 * rho_l * v^2 / l);
    Tli = 350; % Example value, to be calculated based on heat dumped
    
    % Update variables for next iteration
    pl1 = Pli;
    Tl1 = Tli;
    x = x + delta_x;
end

% Step 12: Check structural integrity
% Compute stresses and check against allowable limits
sigma_t = pl1 * pg * w / tw^2 + Ea * q * tw / (2*(1 - v_v)*k);
sigma_l = Ea * (Thot - Tcold);

% Check if σl ≤ 0.9σt for good design
if sigma_l <= 0.9 * sigma_t
    disp('Structural integrity is within limits.');
else
    disp('Structural integrity exceeds limits.');
end

% Calculate buckling stress
sigma_b = Ea * Ec * tw / De * (3*(1 - v_v^2))^0.5;

% Display buckling stress
disp(['Buckling stress: ', num2str(sigma_b), ' Pa']);
