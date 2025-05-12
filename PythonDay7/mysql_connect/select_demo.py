# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="admin",
database = "pydb"
)

# preparing a cursor object
cursorObject = dataBase.cursor()



query = "SELECT * FROM STUDENT where AGE >=20"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
	print(x)

# disconnecting from server
dataBase.close()
