#multi level

class  A():
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2




class  B(A):
      def __init__(self, a1, a2 , b1 , b2):
          super().__init__(a1, a2)
          self.b1 = b1
          self.b2 = b2 

   
       
class  C(B):
    
    def  __init__(self, a1, a2, b1, b2 ,c1):
        super().__init__(a1, a2, b1, b2)
        self.c1 = c1


cobj = C('A1','A2','B1','B2','C1')

print(cobj.__dict__)


#multiple inheritance

class  E():
    def __init__(self,e1):
       self.e1 = e1


class D(A,E): 
    def __init__(self, a1, a2,e1):
        self.a1 = a1
        self.a2 = a2
        self.e1 = e1
       


dobj = D('A1','A2','E1')

print(dobj.__dict__)       