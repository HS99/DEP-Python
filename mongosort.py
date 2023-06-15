#Python MongoDB Sort
#Sort the Result - Use the sort() method to sort the result in ascending or descending order.
#The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).

#Sort the result alphabetically by name
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")
print("Sort by name in ascending order")
for x in mydoc:
  print(x)

#Sort Descending - Use the value -1 as the second parameter to sort descending.
#sort("name", 1) #ascending and sort("name", -1) #descending

#Sort the result reverse alphabetically by name
mydoc = mycol.find().sort("name", -1)
print("Sort by name in descending order")
for x in mydoc:
  print(x)