# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:36:33 2020

@author: skuma
"""
def birthday_paradox(i):
    if i==0 or i==1:
        return 0
    else:
        p = 1
        for j in range(i):
            p = p*(365-j)/365
    return (1-p)
        
import numpy as np
import matplotlib.pyplot as plt
import xlwt
from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0,'People')
sheet1.write(0,1,'Probability')

no_people = 75
x = np.linspace(0, no_people, no_people+1)
p = [1]*(no_people+1)

for i in range(no_people+1):
    p[i] = birthday_paradox(i)
    sheet1.write(i+1, 0, i)
    sheet1.write(i+1, 1, p[i])

n = input('Enter no. of people in room: ')
prob = round(100*birthday_paradox(int(n)),2)
wb.save('Birthday_Paradox.xls')

print('The chances of atleast 2 people sharing their birthday in a room of',n,'people is', prob,'%')

plt.plot(x, p, 'b--')
plt.plot(np.linspace(0, 23, 24), [0.50]*24)
plt.plot([23]*50, np.linspace(0, 0.50, 50))
plt.xlabel('No. of people in room')
plt.ylabel('Probability of atleast 2 people sharing bday')
plt.title('Birthday Paradox')
plt.legend(['Graph','0.50','23 people'], loc="lower right")
plt.grid()
#plt.show()
