num = float(input("\nEnter a number: "))

if num % 1 == 0:
    num = int(num)

print("\nOutput = ",end="")

print( "{:,}".format(num), end="\n\n" )

# Alternatively
# print(f"{num:,}", end="\n\n")
# can also be used


# float precision in python till 53 bits
# or about 16/17 digits of precision

# This is because python uses double precision
# floats

# So float to int conversion in the program
# will give the right/expected value till
# 16/17 digits, after which it would not
# give the correct/expected result
