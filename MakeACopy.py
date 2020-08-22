original_file_name = input("Enter the name/path of the file you want to make a copy of: ")

original_file = open(original_file_name)


copy_file_name = original_file_name.split(".")
copy_file_name = copy_file_name[0] + "-COPY." + copy_file_name[1]

copy_file = open(copy_file_name,"x")
copy_file.write(original_file.read())

print("\nTask successful!")
