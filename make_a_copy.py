original_file_name = input("Enter the name/path of the file you want to make a copy of: ")
original_file_name = original_file_name.strip()

original_file = open(original_file_name)



# Setting the file name of the copy file

ofn_list = original_file_name.split(".")
extension_name = ofn_list[-1]

len_of_original_file_name = len(original_file_name) - len(extension_name) - 1

copy_file_name = original_file_name[:len_of_original_file_name] + "-COPY." + extension_name



# Writing to the copy file
# "w" permission to make sure the program works even if the copy file already exists
copy_file = open(copy_file_name,"w")
copy_file.write(original_file.read())



# Closing the files
original_file.close()
copy_file.close()

print("\nTask successful!")
