
import re

def  f1():

 txt = "Python shell  scripting lang is python which is functional and object oriented"

 matchObj =  re.match(r'Python',txt)    
 print (matchObj.start(), matchObj.end())
 print ("matchObj.group() : ", matchObj.group())


f1() 