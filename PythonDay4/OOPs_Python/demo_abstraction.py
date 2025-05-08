

from abc import ABC , abstractmethod

#demo is a abstract class
class  demo(ABC):

     @abstractmethod
     def method1(self):
      print ("abstract method")
      return
     
     def method2(self):
      print ("concrete method")



class   child(demo):
  
     def method1(self):
      super().method1()
      print ("abstract method is overriden by child class")
      return
     

obj = child()

obj.method1()

