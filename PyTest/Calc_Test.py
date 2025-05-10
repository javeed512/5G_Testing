import pytest
from Calc  import add , sub , mul , div

#before all test cases
def  test_setup():
     print('before all test cases')
     print('connect to the DB')

#after all test cases
def  test_tearup():
       print('after all test cases finished') 
       print('dis-connect from DB')

def  test_add():
   assert  add(2,3) != 10



def  test_sub():
   assert  sub(3,1) == 2



def  test_mul():
   assert  mul(2,3) == 6



def  test_div():
   assert  div(9,3) == 3        

 
   