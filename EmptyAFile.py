# truncating a file
filename = input("Enter a filename/path: ")

# opening the file with write permission automatically truncates it
file_obj = open(filename, "w")

file_obj.close()
