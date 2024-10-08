# Vehicle Class
class Vehicle:
    def __init__(self, color):  #instance variable
        self.color = color      # Store the color of the vehicle
    
    def getColor(self):
        return self.color       # Return the vehicle color
    
    def __str__(self):
        return f"This vehicle is {self.color}"  # Describe the vehicle

class Car(Vehicle):  #inheritance from the vehicle
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)                    # Use the Vehicle's init for color
        self.has_winter_tires = has_winter_tires   # Has winter tires or not
    
    def __str__(self):
        return super().__str__() + f"\nHas winter tires: {self.has_winter_tires}"

class Truck(Vehicle):    #inheritance from Vehicle
    def __init__(self, color, has_trailer=False):
        super().__init__(color)         # get the color from vehicle
        self.has_trailer = has_trailer  # Has trailer or not
    
    def __str__(self):
        return super().__str__() + f"\nHas trailer: {self.has_trailer}"

class Garage:
    def __init__(self):
        self.parked_vehicle = None  # No vehicle in the garage at first
    
    def setVehicle(self, parked):
        self.parked_vehicle = parked  # Park a vehicle in the garage
    
    def __str__(self):
        if self.parked_vehicle:
            return "Description of the parked vehicle:\n" + str(self.parked_vehicle)
        else:
            return "The garage is empty."


class GarageTester:
    @staticmethod
    def getExample():
        truck = Truck("black", has_trailer=False)  # Create a black truck without trailer
        garage = Garage()  # Create a garage
        garage.setVehicle(truck)  # Park the truck in the garage
        print(garage)  # Show what's in the# Vehicle Class
class Vehicle:
    def __init__(self, color):
        self.color = color  # Store the color of the vehicle
    
    def getColor(self):
        return self.color  # Return the vehicle color
    
    def __str__(self):
        return f"This vehicle is {self.color}"  # Describe the vehicle


# Car Class (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)  # Use the Vehicle's init for color
        self.has_winter_tires = has_winter_tires  # Has winter tires or not
    
    def __str__(self):
        return super().__str__() + f"\nHas winter tires: {self.has_winter_tires}"


# Truck Class (inherits from Vehicle)
class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)  # Use the Vehicle's init for color
        self.has_trailer = has_trailer  # Has trailer or not
    
    def __str__(self):
        return super().__str__() + f"\nHas trailer: {self.has_trailer}"


# Garage Class
class Garage:
    def __init__(self):
        self.parked_vehicle = None  # No vehicle in the garage at first
    
    def setVehicle(self, parked):
        self.parked_vehicle = parked  # Park a vehicle in the garage
    
    def __str__(self):
        if self.parked_vehicle:
            return "Description of the parked vehicle:\n" + str(self.parked_vehicle)
        else:
            return "The garage is empty."


# GarageTester Class
class GarageTester:
    @staticmethod
    def getExample():
        truck = Truck("red", has_trailer=False)  
        garage = Garage()  
        garage.setVehicle(truck)  
        print(garage) 


# Customer Class
class Customer:
    def __init__(self, name, address):
        self.name = name  # Store the customer's name
        self.address = address  # Store the customer's address
    
    def __str__(self):
        return f"Customer Name: {self.name}, Address: {self.address}"


if __name__ == "__main__":
    GarageTester.getExample()  # Test the garage system

    customer = Customer("luqman kyembe", " 3456 wall street")  
    print(customer) 


class Customer:
    def __init__(self, name, address):
        self.name = name         # Store the customer name
        self.address = address    # Store the customer address
    
    def __str__(self):
        return f"Customer Name: {self.name}, Address: {self.address}"

if __name__ == "__main__":
    GarageTester.getExample()  

    customer = Customer("luqman kyembe", "456 wall Street")  
    print(customer) 
