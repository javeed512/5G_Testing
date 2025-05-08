

class employee():
 def __init__(self,name,age,id,salary):
  self.name = name
  self.age = age
  self.salary = salary
  self.id = id
 def earn(self):
  pass
  print("this parent  employee earning")
 
 
class childemployee1(employee):
     
     def __init__(self, name, age, id, salary):
       super().__init__(name, age, id, salary)
   
     def earn(self):
       
       #super().earn()
       print('child has no money')
  
    

emp = employee('king',25,101,5000)

emp.earn()
         
c1 = childemployee1('javeed',20,102,6000)   

c1.earn()

   