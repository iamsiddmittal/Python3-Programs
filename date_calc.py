from datetime import datetime
from datetime import timedelta


# operation = input(f"Enter the operation you want to perform ({ops})\n>>> ")
ops = "add / sub"
op_prompt = "Enter the operation you want to perform (" + ops +")\n>>> "
operation = input(op_prompt)


if operation in ["add", "Add", "ADD"]:
    add_to_date = list(map(int, input("Enter Date (Year Month Day): ").strip().split(" ")))
    add_to_date = datetime(add_to_date[0], add_to_date[1], add_to_date[2])

    add = int(input("Enter Days To Add: "))

    result = add_to_date + timedelta(add)
    print(result)


elif operation in ["sub", "Sub", "SUB", "diff", "Diff", "DIFF"]:
    sub_from_date = list(map(int, input("Enter Date (Year Month Day) To Subtract From: ") \
                                        .strip().split(" ")))
    sub_from_date = datetime(sub_from_date[0], sub_from_date[1], sub_from_date[2])

    sub = list(map(int, input("Enter Date (Year Month Day) To Subtract: ") \
                            .strip().split(" ")))
    sub = datetime(sub[0], sub[1], sub[2])

    result = sub_from_date - sub
    print(result)


else:
    print("Not a valid operation code!!")
