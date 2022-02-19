# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:57:36 2020

@author: skuma
"""

'''
From Statistical Mechanics by Werner Krauth

Buffon's Needle Experiment
n = number of throws
r = number of runs
a = length of needle
b = distance between cracks
theta = angle needle makes to crack
rcenter = center of needles on floor
0  < theta < pi/2
0 < xcenter < b/2

nhits <===  number of hits of needle centered at x, with orientation theta
nhits = 1 if x < a/2 and abs(theta) < arcos(x/(a/2))
      = 0 otherwise
'''

import random
import math
import numpy as np
import matplotlib.pyplot as plt
from xlwt import Workbook
   
r=100
n=50000
a = 4  #needle 2 inches
b = 5  #cracks 2 inch spacing

pi_approx = np.zeros(r)
print("Buffon Needle Experiment (Google it)")  
print("Runs       Number Hits  estimate of pi")
for jj in range(r):
    nhits = 0
    for ii in range(n):
        xcent = random.uniform(0,b/2.0)
        theta = random.uniform(0,math.pi/2)
        xtip  = xcent - (a/2.0)*math.cos(theta)  #use of cosine not historically accurate
        if xtip < 0 :
            nhits += 1
    #print str(jj)+'            '+str(nhits)+'               '+str((6.0/a*float(b))*nhits/n)
    c = 2*a*n
    d = b*nhits
    pi_approx[jj] = c/d
    print(str(jj)+"            "+str(nhits)+"               "+str(c/d))
    plt.plot(np.linspace(1, r, r), pi_approx, 'b--')
    plt.plot(np.linspace(1, r, r), [3.14]*r, 'k--')
    plt.ylim([2.9, 3.3])
    
    
# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Trial')
sheet1.write(0, 1, 'Pi')

for i in range(r):
    sheet1.write(i+1,0,i+1)
    sheet1.write(i+1,1,pi_approx[i])

wb.save('Buffon Needle.xls')