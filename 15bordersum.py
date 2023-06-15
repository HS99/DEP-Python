mylist1=list(map(int,input("Enter elements of array\n"). split()))
mylist1.sort(reverse=False) #arr.sort() also be used.
print("Ascending order array")
print(mylist1)
mylist1.sort(reverse=True)
print("Descending order array")
print(mylist1)

# Using sum()
print("SUM Using sum(): ", sum(mylist1))

# Using sum() start from 50
print("SUM Using sum() after adding 50: ", sum(mylist1,50))

# Using List Comprehension with sum()
print("SUM Using List Comprehension with sum(): ", sum([i for i in mylist1]))

# Using for loop with range
total=0
for i in range(len(mylist1)):
    total=total+mylist1[i]
print("SUM Using for loop with range: ", total)

# Using for loop
total=0
for i in mylist1:
    total=total+i
print("SUM Using for loop: ", total)

# Using add() with for loop
from operator import add
total=0
for i in mylist1:
    total = add(i, total)
print("SUM Using add() with for loop: ", total)

# Using while loop
total=0
i=0
while (i < len(mylist1)):
    total=total+mylist1[i]
    i=i+1
print("SUM Using while loop: ", total)


