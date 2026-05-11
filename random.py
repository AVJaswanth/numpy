import numpy as np

rng=np.random.default_rng(1)
print(rng.integers(1,11,3)) # to generate the same random numbers every time we run the code
print(np.random.uniform(-1,1,(3,2)))