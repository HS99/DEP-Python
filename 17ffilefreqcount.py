file1 = open("freqcount.txt", "w")
# write numbers in the text file
contents1 = "This is text file"
file1.write(contents1)
file1.close()
file2 = open("freqcount.c", "w")
# write numbers in the c file
contents2 = "int main"
file2.write(contents2)
file2.close()
file3 = open("freqcount.py", "w")
# write numbers in the python file
contents3 = "print(hello)"
file3.write(contents3)
file3.close()
file1 = open("freqcount.txt", "r")
a=[]
b={}
for i in file1:
    for j in range(0,len(i)):
        a.append(i[j])
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
c=file1.name.split(".")
if c[1]=="txt":
    print("It is a text file")
elif c[1]=="c":
    print("It is a c file")
else:
    print("It is a python file")
file1.close()
file3 = open("freqcount.py", "r")
a=[]
b={}
for i in file3:
    for j in range(0,len(i)):
        a.append(i[j])
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
c=file3.name.split(".")
if c[1]=="txt":
    print("It is a text file")
elif c[1]=="c":
    print("It is a c file")
else:
    print("It is a python file")
file3.close()