import numpy as np

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
print(x)
print(x < 6)
