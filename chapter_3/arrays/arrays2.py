import numpy as np

vec1 = np.arange(1, 10)
print(vec1)
grid = vec1.reshape((3, 3))
print(grid)

x = np.array([1, 2, 3])
print(x)
x.reshape((1, 3))
print(x)
print(x[np.newaxis, :])
print(x.reshape((3, 1)))
print(x[:, np.newaxis])

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y]))

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7], [6, 5, 4]])
# vertically stack the arrays
print(np.vstack([x, grid]))
# horizontally stack the arrays
y = np.array([[99], [99]])
print(np.hstack([grid, y]))
