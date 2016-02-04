from datetime import datetime
from dateutil import parser

date1 = datetime(year=2015, month=7, day=4)
print(date1.strftime('%A'))

date2 = parser.parse("4th of July, 2015")
print(date2)
