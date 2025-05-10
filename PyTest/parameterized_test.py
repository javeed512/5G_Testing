
import pytest

from Calc import add , sub

@pytest.mark.parametrize( "n1,n2,n3", [(2,3,5) , (-1,-2,-3) ,(5,-4,1)  ,(0,0,0)])
def   test_add_params(n1,n2,n3):

   assert  add(n1,n2)  == n3