import numpy as np

np.random.seed(2)
print(np.random.rand())
print(np.random.rand(3,3))
print(np.random.randint(0, 10, size=10))
print(np.random.random_integers(0, 10, size=10))
x = np.arange(10)
print(np.random.permutation(x))
print(np.random.choice(x, 10, replace=True))
np.random.shuffle(x)
print(x)
