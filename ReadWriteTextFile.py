# Open a file
fo = open("text.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
# Close opend file
fo.close()
fo = open("text.txt", "r+")
str = fo.read();
print("Read String is : ", str)
# Close opend file
fo.close()