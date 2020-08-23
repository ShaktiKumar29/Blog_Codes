import matplotlib.pyplot as plt
import numpy as np
p = [1]*100
reqd_prob = [0]*100
#Calculate for a range of values
for x in range(1, 101):
    for i in range(1, x+1):
        p[x-1] = p[x-1]*(365-(i-1))/365
    reqd_prob[x-1] = 1-p[x-1]

#Calculate probability for a single value
no_room = int(input("Enter number of people in room: "))
prob = 1
for i in range(1, no_room+1):
    prob = prob*(365-(i-1))/365
reqd_prob_single = 1-prob
print("There is a", round(reqd_prob_single*100, 2), "% chance that 2 people will have the same birthday in a room with", no_room,"people")

plt.xlim([0, 100])
plt.ylim([0, 1.05])
plt.plot(range(1, 101), reqd_prob, 'b-*', linewidth=1.5, markersize=4)
plt.plot([23]*50, np.linspace(0, 0.5, 50),'k--', label="50% prob@23")
plt.plot(range(0, 24), [0.5]*24,'k--')
plt.plot([32]*50, np.linspace(0, 0.75, 50),'k--', label="75% prob@32")
plt.plot(range(0, 33), [0.75]*33,'k--')
plt.plot([41]*50, np.linspace(0, 0.9, 50),'k--', label="90% prob@41")
plt.plot(range(0, 42), [0.90]*42,'k--')
plt.plot([60]*50, np.linspace(0, 0.99, 50),'k--', label="99% prob@60")
plt.plot(range(0, 61), [0.99]*61,'k--')
plt.grid(True)
plt.title('Birthday Paradox')
plt.xlabel('No. of people in room')
plt.ylabel('Probability of 2 people sharing bday')

plt.legend()

plt.show()
