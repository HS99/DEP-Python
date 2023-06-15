#!/usr/bin/python3
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num%2==0:
        print ('the list contains an even number')
        break
else:
    print ('the list does not contain even number')
############
#!/usr/bin/python3
for letter in 'Python': # traversal of a string sequence
    print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple', 'mango']
for fruit in fruits: # traversal of List sequence
    print ('Current fruit :', fruit)
print ("Good bye!")
########
#!/usr/bin/python3
import sys
for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print (k, end=' ')
    print()
###############
#!/usr/bin/python3
count = 0
while count < 5:
    print (count, " is less than 5")
    count = count + 1
else:
    print (count, " is not less than 5")
######################
#!/usr/bin/python3
for letter in 'Python': # First Example
    if letter == 'h':
        break
    print ('Current Letter :', letter)
var = 10 # Second Example
while var > 0:
    print ('Current variable value :', var)
    var = var-1
    if var == 5:
       break
print ("Good bye!")
###########################
#!/usr/bin/python3
no=int(input('any number: '))
numbers=[11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num==no:
        print ('number found in list')
        break
else:
    print ('number not found in list')
######################
#!/usr/bin/python3
for letter in 'Python': # First Example
    if letter == 'h':
        continue
    print ('Current Letter :', letter)
var = 10 # Second Example
while var > 0:
    var = var -1
    if var == 5:
        continue
    print ('Current variable value :', var)
print ("Good bye!")
################
#!/usr/bin/python3
for letter in 'Python':
    if letter == 'h':
        pass
        print ('This is pass block')
    print ('Current Letter :', letter)
print ("Good bye!")
#######################
#!/usr/bin/python3
# Function definition is here
def printme( str ):
    "This prints a passed string into this function"
    print (str)
    return
# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")
#############
#!/usr/bin/python3
# Function definition is here
def changeme( mylist ):
    "This changes a passed list into this function"
    print ("Values inside the function before change: ", mylist)
    mylist[2]=50
    print ("Values inside the function after change: ", mylist)
    return
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
########################
#!/usr/bin/python3
# Function definition is here
def changeme( mylist ):
    "This changes a passed list into this function"
    mylist = [1,2,3,4] # This would assi new reference in mylist
    print ("Values inside the function: ", mylist)
    return
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
########################
#!/usr/bin/python3
# Function definition is here
def printme( str ):
    "This prints a passed string into this function"
    print (str)
    return
# Now you can call printme function
#printme()
####################
import random
random.seed(2)
print('Generating 5 random numbers: ')
print([random.randint(1, 300) for r in range(6)])
# Reseting the seed value to 1
random.seed(1)
# We will get the same numbers as before
print([random.randint(1, 300) for i in range(6)])
#########################
def isPalindrome(s):
  s1 = s[::-1]
  print(s1)
  return s == s1

# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
  print("Yes")
else:
  print("No")



