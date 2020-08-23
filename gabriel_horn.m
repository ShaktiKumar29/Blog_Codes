clc
clear all
close all

x = 1:0.01:100;
y=1./x;
y1=-y;
plot(x,y,'k-',"markersize",100)
hold on
plot(x,y1,'k-',"markersize",100)
ylim([-1.5,1.5])
grid on