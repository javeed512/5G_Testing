def  read():

  name = input('Enter your name')

  myage = input('Enter your age')

  print('Welcome ',name)

  print(type(myage))

  print('Hello {fname}  , Your age is : {age}'.format(fname= name,age=myage))


  txt = "your age is = {age}"

  print(txt.format(age=31))

  txt1 = "your age is = {:n}"

  print(txt1.format(30))

  txt = "We have {:<8} chickens."
  print(txt.format(49))
 

read()  
print('function is called')
