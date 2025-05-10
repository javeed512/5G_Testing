
import pytest
from Wallet  import Wallet , InsufficientAmountExp

# test_wallet.py

@pytest.fixture
def my_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet(100)

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 120),
    (20, 2, 118),
])
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected