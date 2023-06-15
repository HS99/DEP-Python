#Usimg operators
x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))
result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)
#Using Built in function
import math
a=input("enter first coordinate : ")
p1 = a.split(",")
b=input("enter second coordinate : ")
p2 = b.split(",")
distance = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )
print("distance between ", a,"and", b, "is",distance)