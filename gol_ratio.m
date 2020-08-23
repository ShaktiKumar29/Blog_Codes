clc
clear all
close all

no_iter = 30;
s = 1;
c = zeros(1,no_iter);
gol_rat = zeros(1,no_iter-1);
c(1) = 1;
c(2) = 1;
for i=3:no_iter+1
  c(i) = c(i-1)+c(i-2);
  gol_rat(i-2) = c(i-1)/c(i-2);
endfor
plot(s:no_iter-1, gol_rat(s:no_iter-1), 'b-*')
hold on
plot(1:0.1:no_iter-1, (1+sqrt(5))/2,'-', "markersize", 10)
xlabel('No. of Fibonacci terms')
ylabel('Ratio of consecutive terms')
xlim([1 no_iter-1])
grid on