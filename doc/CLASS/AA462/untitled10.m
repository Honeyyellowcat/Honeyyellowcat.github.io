% Constants
g = 9.81; % gravitational constant (m/s^2)
J = 4186; % Joule's constant (J/kg*K)

% Copper Properties (modify as needed)
thermal_conductivity_copper = 401; % Thermal conductivity of copper (W/m*K)
specific_heat_capacity_copper = 385; % Specific heat capacity of copper (J/kg*K)

% Example Values (modify as needed)
PI = 30e3; % Power input (W)
w = 0.1; % Propellant flow rate (kg/s)
Po = 1; % Plenum-chamber pressure (atm)
Tgas = 300; % Gas temperature (K)
Tw = 300; % Wall temperature (K)

% Properties of Hydrogen (modify as needed)
Hex = 0; % Neglecting thermal energy at nozzle exit for simplicity
HF = 0; % Frozen-flow enthalpy (cal/g)
Hgas = 30; % Gas enthalpy (cal/g) - Example value

% Regenerative Cooling Parameters
A = 0.9; % Arc heater efficiency
F = 0.8; % Frozen-flow efficiency
AN = 0.01; % Inside surface area of thrust or nozzle (sq cm)

% Preallocate arrays for storing results
regen_fraction = 0:0.01:1;
passive_cooling = zeros(size(regen_fraction));

% Loop over regenerative fractions
for i = 1:length(regen_fraction)
    E = regen_fraction(i); % Regenerative fraction
    
    % Power Balance Equations
    Pex = PI * A; % Thermal power loss (available energy not converted to kinetic energy)
    PQ = 0.5 * w * g * (1 - F); % Nozzle-heat power loss (example - modify as needed)
    PR = E * (PI + PQ); % Power absorbed regeneratively
    
    % Determine if passive cooling is possible for portions of the nozzle
    if PR >= (PI + PQ)
        passive_cooling(i) = 1; % Passive cooling possible
    else
        passive_cooling(i) = 0; % Passive cooling not possible
    end
end

% Find the switch point
switch_point = find(passive_cooling, 1, 'first');
switch_fraction = regen_fraction(switch_point);

% Display the switch point
disp(['Passive cooling is possible for portions of the nozzle beyond epsilon = ' num2str(switch_fraction)]);

% Plotting
plot(regen_fraction, passive_cooling, '-o');
xlabel('Regenerative Fraction');
ylabel('Passive Cooling Possibility');
title('Switch from Active to Passive Cooling');



