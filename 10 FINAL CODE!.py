# numpy and matplotlib imported.
import numpy as np
import matplotlib.pyplot as plt
#No seed imported this time cause we want it to be completely random
# Simulate random walk 10000 times
all_walks = []
for i in range(10000) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness              
        if np.random.rand() <= 0.001 :     
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]  # last sublist that has last step at end of 100 throws

# Plot histogram of ends, display plot 
plt.hist(ends)
plt.show()

#Mean of values of last step
print("The mean value of steps at the end of 100 throws is :" + str(np.mean(ends)))

#To Calculate Odds of going over step 60
print("The Odds of winning the bet is ::" + str(np.mean(ends >= 60)))                       
