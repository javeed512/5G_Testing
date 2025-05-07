def  div(a,b):
 try:  
    
  print("div result " , (a/b) )  
 except:  
  print('Some error occurred.')
  print('sorry you cannot div number by zero')  

 finally: 
   print('very very imp code , closing files or close DB connectio or clean memory')

print("Out of try except blocks.")  

div(10,0)