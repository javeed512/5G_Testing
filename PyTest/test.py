
from Wallet import  Wallet 

class  Test():



 def test():
 
     w  = Wallet() 
  
     w.check_balance()
     w.add_cash(200)
     w.check_balance()

     w.add_cash(700)
     w.check_balance()

     w.spend_cash(400)
     w.check_balance()

    
     w.spend_cash(650)


 test()   

     
     

