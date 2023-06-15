#Simple implementation
n = input("Enter name of student: ")
c = input("Enter class of student: ")
a = int(input("Enter age of student: "))
print("Name:", n, "Class:", c, "Age:", a)
print()
print("Name:", n)
print("Class:", c)
print("Age:", a)
#Using Functions
def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()