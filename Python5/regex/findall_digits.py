

#program to extract numbers from a string
 #program to extract numbers from a string
import re
def   f1():
  string = 'hello 12 hi 89. Howdy 34'
  pattern = '\D+'
  result = re.findall(pattern, string)
 
  print(result) 


f1()
 