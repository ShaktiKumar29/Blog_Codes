# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:15:06 2020

@author: skuma
"""
import matplotlib.pyplot as plt

x = int(input("Enter number: "))
step_value = []
step_value.append(x)
i = 0

while x!=1:
    if x%2 == 0:
        x = x/2
        step_value.append(x)
        i+=1
    else:
        x = 3*x+1
        step_value.append(x)
        i+=1
        
print(max(step_value))
print(i)
plt.plot(step_value)
plt.xlabel('Step Number')
plt.ylabel('Value')
plt.grid(True)