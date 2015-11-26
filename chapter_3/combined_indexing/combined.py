import numpy as np
rand = np.random.RandomState(42)

X = np.arange(12).reshape((3, 4))
print(X)
print(X[1:], [2, 0, 1])
X = rand.randint(10, size=(3, 4))
print(X)
X[np.where(X % 2 == 0)]
