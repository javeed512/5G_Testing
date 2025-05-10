
import pytest

# business logic method
def  add(a,b):
    return a+b

#test  method
def  test_add():
   
  actual_value = add(5,15)
  expected_value = 20

  assert actual_value == expected_value