
#from public_demo import Employee

#from private_demo import Employee

from protected_demo import Employee

class Test(Employee):

        def __init__(self):
                pass
        

emp = Employee('javeed',5000) 

print(emp._ename)  #with in package

print(emp.getEname())
print(emp.getSalary())


emp.setEname('javeed khan')
emp.setSalary(12000)
    
print(emp.getEname())
print(emp.getSalary())

emp.hello()
Employee.hello()