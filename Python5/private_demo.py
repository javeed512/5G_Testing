

class Employee():

    def   __init__(self,ename,salary):
            self.__ename = ename   # private ename ,salary
            self.__salary = salary

    


    def    getSalary(self):
                return  self.__salary  
    

    def    getEname(self):
                  return self.__ename              

 
    def   setEname(self,ename):
           self.__ename = ename

    
    def   setSalary(self,salary):
		   self.__salary = salary


    