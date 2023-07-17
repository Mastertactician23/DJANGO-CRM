import mysql.connector
dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password123'


	)

# prepare cursor object
cursorObject = dataBase.cursor()

# create databse
cursorObject.execute("CREATE DATABASE crmdb")

print("All good!")

