from datetime import datetime
from dateutil import parser
import numpy as np
import pandas as pd

date1 = datetime(year=2015, month=7, day=4)
print(date1.strftime('%A'))

date2 = parser.parse("4th of July, 2015")
print(date2)

date = np.array('2015-07-04', dtype=np.datetime64)
print(date)
print(date + np.arange(12))
print(np.datetime64('2015-07-04 12:59:59.50', 'ns'))

date = pd.to_datetime("4th of July, 2015")
print(date.strftime('%A'))
print(date + pd.to_timedelta(np.arange(12), 'D'))
