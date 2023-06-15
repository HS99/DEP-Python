import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="manager",
    database="hsdatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE name ='Ben'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print('Before Update')
for x in myresult:
  print(x)
#sql = "UPDATE customers SET address = 'Canyon 123' WHERE name = 'Ben'"
#mycursor.execute(sql)
sql = "UPDATE customers SET address = %s WHERE name = %s"
val = ("Valley 345", "Ben")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
sql = "SELECT * FROM customers WHERE name ='Ben'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print('After Update')
for x in myresult:
  print(x)