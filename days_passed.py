### Days passed from the beginning of this year

from datetime import datetime

now = datetime.now()
this_year = now.year

days_passed = now - datetime(this_year,1,1) #datetime(year,month,day)

print(days_passed,"have passed since the beginning of this year!",sep="\n")
