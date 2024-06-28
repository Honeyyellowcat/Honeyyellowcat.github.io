clc
clear
close all

% Constants
h_l = 500; % Heat transfer coefficient for liquid oxygen (W/m^2*K)
h_g = 100; % Heat transfer coefficient for gaseous hydrogen (W/m^2*K)
T_r = 293; % Regenerative cooling jacket temperature (K)
T_l = 90;  % Liquid oxygen temperature (K)

% Calculation
Twg = (h_g * T_r + h_l * T_l) / (h_l + h_g);

% Check if Twg is less than T_l
if Twg < T_l
    epsilon = (h_g / h_l) * T_r + T_l;
    disp(['Passive cooling is possible for portions of the nozzle beyond ϵ = ' num2str(epsilon) ]);
else
    epsilon = (h_g / h_l) * T_r + T_l;
    disp(['Active Cooling System is Active. Epsilon = ' num2str(epsilon) ]);
end
