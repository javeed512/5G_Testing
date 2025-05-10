
class InsufficientAmountExp(Exception):
    pass


class Wallet():

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
          try:
           raise InsufficientAmountExp('Not enough available to spend {}'.format(amount))
          except:
            print('Sorry Insuffiecient Amount , cannot spend more')  
        self.balance -= amount

    def add_cash(self, amount):
        print('cash added ',amount)
        self.balance += amount


    def   check_balance(self):
            print('Balance is : ',self.balance)
            return self.balance