import numpy as np
import pandas as pd

index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                          '2015-07-04', '2015-08-04'])
data = pd.Series([0, 1, 2, 3], index=index)
print(data)
dates = pd.to_datetime([pd.datetime(2015, 7, 3), '4th of July, 2015',
    '2015-Jul-6', '07-07-2015', '20150708'])
print(dates)
print(dates.to_period('D'))
print(dates - dates[0])
