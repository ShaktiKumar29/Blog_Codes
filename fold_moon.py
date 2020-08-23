# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:42:55 2020

@author: skuma
"""

import numpy as np
import matplotlib.pyplot as plt

no_of_folds = 42
thickness = 1e-7 #0.1mm in km
dist_moon = [1]*(no_of_folds+1)

for i in range(no_of_folds+1):
    dist_moon[i] = thickness*pow(2,i)

plt.plot(range(no_of_folds+1), dist_moon, 'b-*')
plt.plot(np.linspace(0, 42, 43), [384000]*43)
plt.xlabel('Number of folds')
plt.ylabel('Distance(km)')
plt.title('Reaching The Moon Using Just A Piece of Paper')
plt.grid()
plt.show()    
