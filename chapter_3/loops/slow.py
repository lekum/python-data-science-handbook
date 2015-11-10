import numpy as np
np.random.seed(0)

def compute_reciporicals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1 / values[i]
    return output

values = np.random.randint(1, 10, size=1E06)
print(compute_reciporicals(values))
