
class  employee():
    def  __init__(self,id,name,age,salary):    # id,name,age,salary are parameters
        self.eid = id    # eid is an instance var
        self.ename = name   # self keyword refers to current class obj
        self.age = age    # self.age is instance var and age is local var
        self.salary = salary

        #print(self)


emp1 = employee(101,'harshit',22,4000)
print(emp1.eid)
print(emp1.ename)
print(emp1.age)
print(emp1.salary)

emp2 = employee(102,'javeed',30,7000)

print(emp2.__dict__)

