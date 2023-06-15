with open('fileseek1.txt', "r") as fp:
    # Moving the file handle to 6th character
    fp.seek(6)
    # read file
    print(fp.read())

print('\nOpen file in write and read mode w+')
with open('fileseek1.txt', "w+") as fp:
    # add content
    fp.write('My First Line\n')
    fp.write('My Second Line')
    # move pointer to the beginning
    fp.seek(0)
    # read file
    print(fp.read())

print('\nOpen file for reading and writing  a+')
with open('fileseek1.txt', "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2)

    # Inserting new content to the end of the file
    fp.write("\nThis content is added to the end of the file")

    # moving to the beginning
    # again read the whole file
    fp.seek(0)
    print(fp.read())

print('\nOpen file for reading in Binary mode')
with open('fileseek1-2.txt', "rb") as fp:
    # Move the file handle to the 5th character
    # from the beginning of the file
    fp.seek(3)
    # read 5 bytes and convert it to string
    print(fp.read(5).decode("utf-8"))

    # Move the fp 10 points ahead from current position
    # read 5 bytes and convert it to string
    fp.seek(10, 1)
    # again read 6 bytes
    print(fp.read(6).decode("utf-8"))

print('\nOpen file for reading in binary mode')
with open('fileseek1-2.txt', "rb") as fp:
    # Move in reverse direction
    # move to the 40th character from the end of the file
    fp.seek(-40, 2)
    # read 11 bytes and convert it to string
    print(fp.read(11).decode("utf-8"))

print('\nOpen file for reading in binary mode')
with open('fileseek1-2.txt', "rb") as fp:
    # read first 8 bytes
    print(fp.read(8).decode('utf-8'))
    # Move in reverse direction
    # move to the 5th behind from current position
    fp.seek(-5, 1)
    # read 10 bytes and convert it to string
    print(fp.read(10).decode("utf-8"))