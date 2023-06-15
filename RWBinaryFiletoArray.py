#Python read a binary file to an array
file=open("array.bin","wb")
num=[2,4,6,8,10]
array=bytearray(num)
file.write(array)
file.close()
file=open("array.bin","rb")
number=list(file.read())
print (number)
file.close()
