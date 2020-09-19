from datetime import datetime

now = datetime.now()
new_year = now.year + 1

# timedelta object
days_left = datetime(new_year,1,1) - datetime(now.year, now.month, now.day)

# datetime object
exact_time = (datetime(new_year,1,1) - now) #datetime(year,month,day)

print()
print(f"Days left till new year: {days_left.days}", end="\n\n")
print(f"Exact time: {exact_time}", end="\n\n")
