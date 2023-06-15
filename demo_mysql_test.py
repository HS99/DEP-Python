import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="manager",
  database="hsdatabase"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE hsdatabase")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)