import pandas as pd
import numpy as np

population_dict = {'California': 38332521,
        'Texas': 26448193,
        'New York': 19651127,
        'Florida': 19552860,
        'Illinois': 12882135}
population = pd.Series(population_dict)

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 12882135}
area = pd.Series(area_dict)
states = pd.DataFrame({'population': population, 'area': area})
print(states)
print()
print(pd.DataFrame(population, columns=['population']))
print()
data = [{'a': i, 'b': 2 * i} for i in range(3)]
print(data)
print(pd.DataFrame(data))
print()
print(pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]))
print()
print(pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 'b', 'c']))
