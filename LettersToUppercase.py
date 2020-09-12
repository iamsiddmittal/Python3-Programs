# Works for file/string/word/phrase

i = input("Enter word/phrase/filename: ")

try:
    f_obj = open(i, "r+")
    new_content = f_obj.read().upper()

    f_obj.seek(0)
    f_obj.write( new_content )

    print("Content inside the file has been converted into uppercase")
except:
    print( i.upper() )
