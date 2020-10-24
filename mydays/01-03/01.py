from datetime import datetime
from datetime import date
from datetime import timedelta


today = datetime.today()
print(today)

t = timedelta(days=4, hours=10)
second = timedelta(seconds=1)

seconds = t/second
print(seconds)
