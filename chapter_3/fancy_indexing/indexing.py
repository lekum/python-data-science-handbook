import numpy as np
rand = np.random.RandomState(42)
x = rand.randint(100, size=10)
print(x)
ind = [3, 7, 4]
print(x[ind])
ind = np.array([[3, 7],
                [4, 5]])
print(x[ind])
