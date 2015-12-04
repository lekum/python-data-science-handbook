import numpy as np
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data)
population_dict = {'California': 38332521,
        'Texas': 26448193,
        'New York': 19651127,
        'Florida': 19552860,
        'Illinois': 12882135}
population = pd.Series(population_dict)
print(population)
print(pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2]))
