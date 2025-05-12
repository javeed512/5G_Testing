
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="admin"
)

print(dataBase)


cursorObj =     dataBase.cursor()

cursorObj.execute("CREATE DATABASE  pydb")




# Disconnecting from the server
dataBase.close()
