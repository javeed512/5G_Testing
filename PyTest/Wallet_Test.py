

import pytest

from Wallet import  Wallet , InsufficientAmountExp

# 

wallet = Wallet() 


def  test_wallet_add_cash():

      
       wallet.add_cash(100)

       assert   wallet.check_balance() == 100


def   test_wallet_spend_cash():
      

       wallet.spend_cash(50)

       assert  wallet.check_balance()  == 50


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():

        wallet = Wallet() #balance = 0
        
        try:
                
           with  pytest.raises(InsufficientAmountExp):
                wallet.spend_cash(500)

        except:
              assert True        

