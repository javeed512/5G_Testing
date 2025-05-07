# Python program to illustrate 
# *args for variable number of arguments 
def myFun(*names):   # var agrs or rest params
 for  name  in names: 
  print(name) 


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

myFun(10,20,30,40)