from random import randint
import numpy as np
import matplotlib.pyplot as plt
import statistics
import datetime
begin_time = datetime.datetime.now()

no_of_trials = [100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000, 50000, 100000, 500000, 1000000, 2500000, 5000000]
dont_switch = [0]*len(no_of_trials)
switch_door = [0]*len(no_of_trials)

for y in range(len(no_of_trials)):
    for x in range(int(no_of_trials[y])):
        #print(" ")
        player_door = randint(1, 3)
        #print("Player has chosen Door", player_door)
        gift_door = randint(1, 3)
        #print("The car is in Door",gift_door)
        if player_door == gift_door:
            #print("The player SHOULD NOT SWITCH")
            dont_switch[y]+=1
        else:
            #print("The player SHOULD SWITCH")
            switch_door[y]+=1
    switch_door[y]/=no_of_trials[y]
    dont_switch[y]/=no_of_trials[y]

print("Switch:", switch_door)
print("Don't Switch:", dont_switch)

# Plot the data
plt.xlim([min(no_of_trials), max(no_of_trials)])
#plt.ylim(0.65, 0.75)
plt.ylim([min(switch_door), max(switch_door)])
plt.grid(True)
plt.semilogx(no_of_trials, switch_door, "b-*", label='linear')
plt.plot(np.linspace(min(no_of_trials), max(no_of_trials), 100), [2/3]*100, 'k--', label='Earth-moon distance')
plt.xlabel('No of iterations')
plt.ylabel('Prob of winning if you switch')
plt.title('Monty Hall Problem - Simulations')

print("Execution time:", datetime.datetime.now() - begin_time)
# Show the plot
plt.show()