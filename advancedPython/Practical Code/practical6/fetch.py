import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "Company"
)

cursor = mydb.cursor()

cursor.execute("select * from Employee;")

# Fetch One
#dataOne = cursor.fetchone()
#print(dataOne)

# Fetch Many
#dataMany = cursor.fetchmany(3)
#for data in dataMany:
#    print(data)

# Fetch All
dataAll = cursor.fetchall()
for data in dataAll:
    print(data)

