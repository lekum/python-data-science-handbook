import numpy as np

def pe(expr):
    print(expr, "=", "\n", eval(expr), "\n")

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
pe("a")
pe("b")
pe("a + b")
pe("a + 5")
pe("a + 5")
M = np.ones((3, 3))
pe("M")
pe("M + a")
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
pe("a")
pe("b")
pe("a + b")
M = np.ones((2, 3))
a = np.arange(3)
pe("a")
pe("M")
pe("a + M")
