# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

#2nd random value for same seed
print(np.random.rand())

#for same seed,it generates same random no.(thus pseudorandom generators)
np.random.seed(123)
print(np.random.rand())
print(np.random.rand())