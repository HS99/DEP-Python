# open file for reading and writing  r+
with open('fileseek1-2.txt', "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2)

    # getting the file handle position
    print('file handle at:', fp.tell())

    # writing new content
    fp.write("\nDemonstrating tell")

    # getting the file handle position
    print('file handle at:', fp.tell())

    # move to the beginning
    fp.seek(0)
    # getting the file handle position
    print('file handle at:', fp.tell())

    # read entire file
    print('***Printing File Content***')
    print(fp.read())
    print('***Done***')

    # getting the file handle position
    print('file handle at:', fp.tell())
