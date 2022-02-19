# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 12:15:07 2020

@author: skuma
"""

import numpy as np
import matplotlib.pyplot as plt
import math

start = 1
end = 10001
step_value = 1
r = -1
x = range(start, end+1, step_value)
count = [0]*len(x)

for i in x:
    t = i
    r+=1
    while t!=1:
        if t%2 == 0: # Even Number
            t = t/2
            count[r]+=1
        else:
            t = 3*t+1
            count[r]+=1
    print(i, "takes", count[r], "to reach 1")

print(max(count))

plt.plot(x, count, 'b-')
plt.grid(True)
plt.title('Collatz Conjecture - No. of steps to reach 1')
plt.xlabel('Number')
plt.ylabel('No. of steps')