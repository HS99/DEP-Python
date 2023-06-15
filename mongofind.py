#Python MongoDB Find
#In MongoDB we use the find() and find_one() methods to find data in a collection.
#Just like the SELECT statement is used to find data in a table in a MySQL database.

#Find One - To select data from a collection in MongoDB, we can use the find_one() method. The find_one() method returns the first occurrence in the selection.
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
print("Find_one")
x = mycol.find_one()
print(x)

#Find All - To select data from a table in MongoDB, we can also use the find() method.
#The find() method returns all occurrences in the selection.
#The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.
print("Find ")
for x in mycol.find():
  print(x)

#Return Only Some Fields - The second parameter of the find() method is an object describing which fields to include in the result.
#This parameter is optional, and if omitted, all fields will be included in the result.
print("Find with parameters")
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

#You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). If you specify a field with the value 0, all other fields get the value 1, and vice versa
print("Find with address parameters")
for x in mycol.find({},{ "address": 0 }):
  print(x)

#You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field)
print("find with error")
for x in mycol.find({},{ "name": 1, "address": 0 }):
  print(x)