# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:25:58 2020

@author: skuma
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 50, (50-1)*100+1)
print(x)
y = 1/x
plt.plot(x, y, 'k-')
plt.plot(x, -y, 'k-')
plt.grid()
plt.show()

