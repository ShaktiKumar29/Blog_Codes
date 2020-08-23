# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:18:08 2020

@author: skuma
"""

def birthday_paradox(i):
    if i==0 or i==1:
        return 0
    else:
        p = 1
        for j in range(i):
            p = p*(365-j)/365
    return (100*(1-p))
        
import numpy as np
import matplotlib.pyplot as plt
import xlwt
from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0,'People')
sheet1.write(0,1,'Actual')
sheet1.write(0,2,'Estimate')
sheet1.write(0,3,'Error')
sheet1.write(0,4,'% Error')

no_people = 75
x = np.linspace(0, no_people, no_people+1)
p_mul = [1]*(no_people+1)
p_approx = [1]*(no_people+1)
err = [1]*(no_people+1)
per_error = [1]*(no_people+1)

for i in range(no_people+1):
    p_mul[i] = birthday_paradox(i)
    p_approx[i] = 100*(1-np.exp(-i*(i-1)/730))
    err[i] = p_mul[i] - p_approx[i]
    per_error[i] = 100*err[i]/p_mul[i]
    sheet1.write(i+1, 0, i)
    sheet1.write(i+1, 1, p_mul[i])
    sheet1.write(i+1, 2, p_approx[i])
    sheet1.write(i+1, 3, err[i])
    sheet1.write(i+1, 4, per_error[i])
wb.save('Birthday_Paradox_Math.xls')

for i in range(no_people):
    if err[i+1]<err[i]:
        break
print(i)

f = plt.figure(1)
plt.plot(x, p_mul, 'b--')
plt.plot(x, p_approx, 'k--')
plt.plot(x, err, 'g--')
plt.xlabel('No. of people in room')
plt.ylabel('Probability of atleast 2 people sharing bday')
plt.title('Birthday Paradox')
plt.legend(['Actual Prob','Estimate Prob','Error'], loc="upper left")
plt.grid()

g = plt.figure(2)
plt.plot(x, err,'b--')
plt.plot(x, per_error, 'k--')
plt.legend(['Error', '% Error'])
plt.title('Error between approx & actual')
plt.grid()
plt.show()
