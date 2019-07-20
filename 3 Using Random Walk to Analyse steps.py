# Numpy is imported, seed is set
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]       #since 1st step is 0

# Complete the 100 steps
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
                          #There's still something wrong: the level at index 15 is negative!