from datetime import datetime
from datetime import timedelta

a = list(map(int, input("Enter Date (Year Month Day): ").split(" ")))

a = datetime(a[0], a[1], a[2])

add = int(input("Enter Days To Add: "))

result = a + timedelta(add)

print(result)
