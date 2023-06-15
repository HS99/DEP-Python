file = open("filereverse.txt", "w")
# write numbers in the text file
contents1 = "This is first line\nThis is second line\nThis is last line"
file.write(contents1)
file.close()
# Open the input file again and get # the content as list to a variable data
with open("filereverse.txt", "r") as myfile:
    contents2 = myfile.readlines()
print("Before Reverse", contents2)
# We will just reverse the # array using following code
contents2 = contents2[::-1]
print("After Reverse", contents2)
