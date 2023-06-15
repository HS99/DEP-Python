import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="manager",
    database="hsdatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM customers")
myresult = mycursor.fetchall()
print('Before Delete')
for x in myresult:
  print(x)
sql = "DELETE FROM customers WHERE name = %s"
nam = ("Ben", )
mycursor.execute(sql, nam)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
mycursor.execute("SELECT name FROM customers")
myresult = mycursor.fetchall()
print('After Delete')
for x in myresult:
  print(x)
