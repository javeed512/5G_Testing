
class  Calc():

     def __init__(self):
          pass
     
     
     def  add(self,a,b):
        print("Addition of a,b :", a+b) 

     def  add(self,a,b,c):        #method overloading  or compile time polymorphism example
        print("Addition of a,b,c :", a+b+c)    


#end user using add() func
c = Calc()

#c.add(5,5,10)