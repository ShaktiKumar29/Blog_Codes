clc
clear all
close all

n = 100;
y = zeros(1,length(n));
for i=1:length(n)
  y(i) = 4*(n(i)+1000)/(n(i)-1);
end
plot(n, y)
#hold on
#plot(1:10:500, e, 'k-*')
grid on
y(end)