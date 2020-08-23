import matplotlib.pyplot as plt
import numpy as np
no_of_folds = 42
thickness = 0.1 #in mm
dist_fold = [0]*(no_of_folds+1)
dist_fold[0] = thickness

for x in range(1, no_of_folds+1):
    dist_fold[x] = thickness*pow(2, x)
    dist_fold[x] = dist_fold[x]*pow(10, -6)

plt.xlim([0, 45])
plt.ylim([0, 500000])
plt.plot(range(no_of_folds+1), dist_fold, 'b-*', label='Distance in each fold')
plt.title('Reaching the moon using a piece of paper')
plt.grid(True)
plt.xlabel('No. of folds')
plt.ylabel('Distance (km)')
plt.plot(np.linspace(0,42,50), [3.84*pow(10,5)]*50, 'k-*', label='Earth-moon distance')
plt.legend()
plt.show()
