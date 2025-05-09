
class Employee():

    def   __init__(self,ename,salary):
            self._ename = ename    # ename, salary are proctected
            self._salary = salary

    @staticmethod
    def    hello():
      
        print('hello am static method')           
 

    
    def    getSalary(self):
                return  self._salary  
    

    def    getEname(self):
                  return self._ename              

 
    def   setEname(self,ename):
           self._ename = ename

    
    def   setSalary(self,salary):
		   self._salary = salary        