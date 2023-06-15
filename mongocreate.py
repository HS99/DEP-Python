#Creating a Database
import pymongo

#To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.
#MongoDB will create the database if it does not exist, and make a connection to it.
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#Create a database called "mydatabase"
mydb = myclient["mydatabase"]
#MongoDB waits until you have created a collection (table), with at least one document (record) before it actually creates the database (and collection).

#Return a list of your system's databases
print(myclient.list_database_names())

#Or you can check a specific database by name
#Check if "mydatabase" exists
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")