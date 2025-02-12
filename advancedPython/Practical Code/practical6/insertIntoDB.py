import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "Company"
)

cursor = mydb.cursor()

cursor.execute("INSERT INTO Employee value( 9, 'John Doe', 105, 72000.00, 4)")
cursor.execute("INSERT INTO Employee value( 10, 'Jane Doe', 105, 72000.00, 4)")
cursor.execute("INSERT INTO Employee value( 11, 'abcd Doe', 105, 72000.00, 5)")

print(cursor.rowcount,"record(s)affected")
mydb.commit()
