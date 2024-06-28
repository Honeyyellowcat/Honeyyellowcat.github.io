clear all

T1= table2array(readtable('T0298.csv'));
A1 = smoothdata(T1(1:7000,13),'gaussian',100);
B1 = smoothdata(T1(1:2360,10),'gaussian',300);

subplot(2,2,1)
hold on
grid on
plot(T1(1:7000,12),T1(1:7000,13),'.','MarkerSize',10)
xlabel('Time (mircosec)')
ylabel('Current (A)')
title('Original Current')

subplot(2,2,2)
hold on
grid on
plot(T1(1:7000,12),A1(1:7000,1),'.','MarkerSize',10)
xlabel('Time (mircosec)')
ylabel('Current (A)')
title('Smoothed Current')

subplot(2,2,3)
hold on
grid on
plot(T1(1:2360,12),T1(1:2360,10),'.','MarkerSize',10)
xlabel('Time (mircosec)')
ylabel('Voltage (V)')
title('Original Voltage')

subplot(2,2,4)
hold on
grid on
plot(T1(1:2360,12),B1(1:2360,1),'.','MarkerSize',10)
xlabel('Time (mircosec)')
ylabel('Voltage (V)')
title('Smoothed Voltage')

%%
clear all

T2= table2array(readtable('T0299.csv'));
A2 = smoothdata(T2(1:15800,14),'gaussian',100);
B2 = smoothdata(T2(1:15000,6),'gaussian',300);

figure(2)
subplot(2,2,1)
hold on
grid on
plot(T2(1:15800,13),T2(1:15800,14),'.','MarkerSize',10)
xlabel('Time (mircosec)')
ylabel('Current (A)')
title('Original Current')

subplot(2,2,2)
hold on
grid on
plot(T2(1:15800,13),A2(1:15800,1),'.','MarkerSize',10)
xlabel('Time (mircosec)')
ylabel('Current (A)')
title('Smoothed Current')

subplot(2,2,3)
hold on
grid on
plot(T2(1:15000,13),T2(1:15000,6),'.','MarkerSize',10)
xlabel('Time (mircosec)')
ylabel('Voltage (V)')
title('Original Voltage')

subplot(2,2,4)
hold on
grid on
plot(T2(1:15000,13),B2(1:15000,1),'.','MarkerSize',10)
xlabel('Time (mircosec)')
ylabel('Voltage (V)')
title('Smoothed Voltage')
