num = float(input("\nEnter a number: "))

if num % 1 == 0:
    num = int(num)

print("\nOutput = ",end="")

print( "{:,}".format(num), end="\n\n" )

# Alternatively
# print(f"{num:,}", end="\n\n")
# can also be used