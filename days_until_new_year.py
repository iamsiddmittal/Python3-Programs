### Days till new year

from datetime import datetime

now = datetime.now()
new_year = now.year + 1

days_left = (datetime(new_year,1,1) - now) #datetime(year,month,day)

print(days_left,"remaining till the next year",sep="\n")
