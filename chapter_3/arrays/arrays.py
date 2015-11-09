import numpy as np
print(np.array([1, 4, 2, 5, 3]))
print(np.zeros(10, dtype=np.int))
print(np.zeros((3, 5), dtype=np.int))
print(np.full((3, 5), np.pi))
print(np.arange(3, 20, 2))
print(np.linspace(3, 20, 5))
print(np.random.random((3, 20)))
print(np.eye(8))
x1 = np.random.randint(10, size=(5, 4))
print(x1)
print(x1[:2, :3])
x1_sub_copy = x1[:2, :3].copy()
print(x1_sub_copy)
x1_sub_copy[0, 0] = 0
print(x1_sub_copy)
print(x1)