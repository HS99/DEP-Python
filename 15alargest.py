a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c
print("\nLargest using if statements")
print(largest, "is the largest of three numbers.")

largest = 0

if a > b and a > c :
    largest = a
elif b > c :
    largest = b
else :
    largest = c
print("\nLargest using if...elif statements")
print(largest, "is the largest of three numbers.")