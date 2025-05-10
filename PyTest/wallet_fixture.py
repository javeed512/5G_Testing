
import pytest
from Wallet  import Wallet , InsufficientAmountExp

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)


def  test_balance(wallet):

   assert  wallet.check_balance() == 20

def  test_add_cash(wallet):
    
    wallet.add_cash(30)
    assert  wallet.check_balance() == 50



def   test_spend_cash(wallet):
     
     print(wallet.check_balance())   
     
     wallet.spend_cash(10)
     assert  True

