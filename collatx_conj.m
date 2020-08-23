clc
clear all
close all

n = 1:2:51;
k = zeros(1,length(n))
n1 = n;
for i=1:length(n)
  i1=i;
  while n(i)!=1
    if rem(n(i),2)==0
      n(i) = n(i)/2;
      k(i1)++;
    else
      n(i) = 3*n(i)+1;
      k(i1)++;
    endif
  endwhile
endfor

plot(n1, k, 'r-*')