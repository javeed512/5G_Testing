
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="admin",
database = "pydb"
)

