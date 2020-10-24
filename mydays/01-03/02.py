from datetime import datetime
from datetime import timedelta
import time

period = input("how long? ")
period = int(period)

workperiod = timedelta(minutes=period)
second = timedelta(seconds=1)
minute = timedelta(minutes=1)

starttime = datetime.now()

while datetime.now() - starttime < workperiod:
    now = datetime.now()
    elapsed = now - starttime 
    remaining = workperiod - elapsed
    totalsec = remaining.seconds

    minutes = round(totalsec/60) - 1
    if minutes < 0: minutes = 0
    seconds = totalsec % 60

    print(minutes,':',seconds)
    time.sleep(1)

print('the end')

