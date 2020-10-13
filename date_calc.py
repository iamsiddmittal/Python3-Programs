from datetime import datetime
from datetime import timedelta

operation = input("Enter the operation you want to perform (add)\n>>> ")

if operation in ["add", "Add", "ADD"]:
    add_to_date = list(map(int, input("Enter Date (Year Month Day): ").strip().split(" ")))
    add_to_date = datetime(add_to_date[0], add_to_date[1], add_to_date[2])

    add = int(input("Enter Days To Add: "))

    result = add_to_date + timedelta(add)
    print(result)

else:
    print("Not a valid operation code!!")
