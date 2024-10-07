
class Vehicle:
    def __init__(self, color):
        self.color = color  
    
    def getColor(self):
        return self.color
        def __str__(self):
            return f"This vehicle is {self.color}"


class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color) 
        self.has_winter_tires = has_winter_tires  
    
    def __str__(self):
        return super().__str__() + f"\nHas winter tires: {self.has_winter_tires}"


class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)  s
        self.has_trailer = has_trailer 
    
    def __str__(self):
        return f"Customer Name: {self.name}, Address: {self.address}"


if __name__ == "__main__":
    GarageTester.getExample()

    customer = Customer("John Doe", "123 Elm Street")
    print(customer)