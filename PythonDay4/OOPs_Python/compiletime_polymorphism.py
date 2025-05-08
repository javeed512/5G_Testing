
#employee1 class with methods
class employee1():
 def name(self):
  print("Harshit is his name")   


 def salary(self):
  print("3000 is his salary")
 def age(self):
  print("22 is his age")
  


#employee2 class with methods

class employee2():
 def name(self):
  print("Rahul is his name")
 def salary(self):
  print("4000 is his salary")
 def age(self):
  print("23 is his age")


def showEmp(obj):   # method overloading 
    obj.name()
    obj.salary()
    obj.age()

def showEmp(obj,city):
     obj.name()  
     print("your city is ",city)    
   

emp1 = employee1()
emp2 = employee2()

#showEmp(emp1)  
#showEmp(emp2) 

showEmp(emp2,'Hyd')

