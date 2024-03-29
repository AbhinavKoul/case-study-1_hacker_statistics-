# Numpy is imported; seed is set
import numpy as np
np.random.seed(123)
# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10):     

    # Code from before
    random_walk = [0]
    for x in range(100) :                    #same activity loop
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)         #all the walks ever taken when the same activity is repeated 10 times
   # will be in the form of lists of list ie. [ [1st random walk],[2nd random walk],[3rd random walk],.......,[10th random walk]]