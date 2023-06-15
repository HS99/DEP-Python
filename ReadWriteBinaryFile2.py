#Python read a binary file line by line
lines='Welcome to python guides'
file=open("document1.txt","wb")
file.write(lines.encode())
file.close()
file=open("document1.txt","rb")
filelines=file.readline()
print(filelines)
file.close()
#Python read a binary file to Ascii
file = open('test.bin', 'w+b')
sentence = 'Hello Python'
file_encode = sentence.encode('ASCII')
file.write(file_encode)
file.seek(0)
bdata = file.read()
print('Binary sentence', bdata)
new_sentence = bdata.decode('ASCII')
print('ASCII sentence', new_sentence)
#Python read a binary file into a NumPy array
#Python read a binary file into CSV

####Not Included#############
#Python read a binary file into a byte array
file = open("array.bin", "rb")
byte = file.read()
while byte:
    print(byte)
    byte = file.read()