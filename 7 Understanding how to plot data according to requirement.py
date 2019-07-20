# numpy and matplotlib imported, seed set.
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
# initialize and populate all_walks
all_walks = []
for i in range(10) :
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
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw  (this has 10 rows and 100 columns) ( nth row has nth occurances of random walk(each random walk having 100 elements))
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()


# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t             (this has 100 rows and 10 columns) (nth row has steps of nth dice throw at diffirent(10) occurances)
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

#UNDERSTANDING THIS IS VERY VERY IMPORTANT:
 # In a 2D List(list of list)
   # no. of rows = no. of index(no. of sub-lists) = x axis on plot
   # no. of columns = no. of values in each sublist = y axis on plot