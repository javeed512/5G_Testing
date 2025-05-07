def func1(): 
 a = 20 
 def func2(): 
  nonlocal a 
  print('func2 ', a) 
 func2() 

 print('func1 ', a) 
func1()