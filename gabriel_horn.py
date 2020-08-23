import numpy as np
import matplotlib.pyplot as plt
n = 10
x = np.linspace(1, n, 1000)
y = 1/x
y1 = -y
plt.xlim([-0.5, n])
plt.ylim([-2, 2])
plt.plot(x, y, 'k-')
plt.plot(x, y1, 'k-')
#plt.title('Reaching the moon using a piece of paper')
#plt.grid(True)
plt.show()