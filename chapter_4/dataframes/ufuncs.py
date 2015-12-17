import pandas as pd
import numpy as np

rng = np.random.RandomState(42)
df = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns=['A', 'B', 'C', 'D'])
print(np.sin(df * np.pi / 4))
