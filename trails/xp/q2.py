class Vehicle:
    def __Init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
class Car(Vehicle):
    def __init__ (self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        
        def fuel(self, amount):
            