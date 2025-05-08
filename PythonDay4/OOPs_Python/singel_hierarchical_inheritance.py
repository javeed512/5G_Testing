
class  Car():
    def __init__(self,fuel,breaks,color,seats):
       self.fuel = fuel
       self.breaks = breaks
       self.color = color
       self.seats = seats

    def  showCarDetails(self):
       
       print(self.__dict__)
          



class   HondaCar(Car):

   def __init__(self, fuel, breaks, color, seats,model,airbags):
      super().__init__(fuel, breaks, color, seats)
      self.model = model
      self.airbags = airbags
      
class   OlaCar(Car):

   def __init__(self, fuel, breaks, color, seats,model,price):
      super().__init__(fuel, breaks, color, seats)
      self.model = model
      self.price = price


car1 = Car('petrol','disc-breaks','white',4)     

print(car1.__dict__)

honda1 = HondaCar('Diesel','auto-breaks','red',7,'A1',True)

print(honda1.__dict__)


olaCar = OlaCar('EV','disc-breaks','black',7,'SUV',1200000)

print(olaCar.__dict__)

car1.showCarDetails()