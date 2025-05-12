

from dbconnect import dataBase

cursorObj = dataBase.cursor()

updateQuery = "UPDATE STUDENT  SET  name = %s , branch = %s , roll = %s , section = %s , age = %s  where sid = %s"

val  = ("nikhil kumar","Computers","998","A+","23","102")




# deleteQuery = "DELETE FROM STUDENT WHERE SID = %s"
# val= ("101")

cursorObj.execute(updateQuery , val)





dataBase.commit()

dataBase.close()