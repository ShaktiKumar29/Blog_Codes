# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:51:30 2020

@author: skuma
"""

import math
import numpy as np
import matplotlib.pyplot as plt

y=[]
theta = np.linspace(0, 3.14, 1000)
for i in range(len(theta)):
    y.append(math.sin(theta[i]))

plt.plot(theta, y)
plt.plot([0]*1000, np.linspace(0, 1, 1000), 'k-')
plt.plot([3.14]*1000, np.linspace(0, 1, 1000), 'k-')
plt.plot(np.linspace(0, 3.14, 1000), [1]*1000, 'k-')
plt.fill_between(theta, y)
plt.xlabel('Angle')
plt.ylabel('d')