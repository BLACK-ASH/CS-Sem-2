import mysql.connector
mydb = mysql.connector.connect(
        host="local host",
        user="root",   
        password="root" 
    )

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
   
