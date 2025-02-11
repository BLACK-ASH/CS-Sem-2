import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "Company"
)

cursor = mydb.cursor()

cursor.execute("delete from Employee where EmpID =11 ")

print(cursor.rowcount,"record(s)affected")
mydb.commit()
