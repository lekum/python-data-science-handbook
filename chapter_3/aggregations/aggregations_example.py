import numpy as np

M = np.random.random((3, 4))
print("M")
print(M)
print("M.sum() =", M.sum())
print("M.min(axis=0) =", M.min(axis=0))
print("M.min(axis=1) =", M.min(axis=1))
print("np.mean(M) =", np.mean(M))
print("np.std(M) =", np.std(M))
