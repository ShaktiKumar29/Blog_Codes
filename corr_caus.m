clc
clear all
close all

x = 1:10;
y = -2*x;
%y = 10*ones(1,10);
%y1 = 20*rand(1,10);
y1 = [21.2, 14.5, 21.2, 16, 9.6, 13.6, 11.4, 7, -1, 2.5]
%y1 = [2.5, -1, 7, 11.4, 13.6, 9.6, 16, 21.2, 14.5, 21.2]

corr(x,y1)
plot(x,y1,'b*', "markersize", 15)
xlim([0 12])
ylim([-2 24])
hold on
plot(x,y,'r--')