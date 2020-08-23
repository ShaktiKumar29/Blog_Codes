clc
clear all
close all

x = 2:2:10;
y = [9, 13, 17, 21, 25];
n = length(x);
%y = a+bx

b1 = (n*sum(x.*y)-(sum(x)*sum(y)));
b2 = n*(sum(x.^2))-(sum(x))^2;
b = b1/b2
a = mean(y) - b*mean(x)

y_hat = a+b*x;

SSE = sum((y-y_hat).^2)
plot(x, y, 'b*')
hold on
plot(x, y_hat, 'r--')
grid on
