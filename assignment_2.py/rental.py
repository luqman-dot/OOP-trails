# Vehicle Class
class Vehicle:
    def __init__(self, color):
        self.color = color  #color store
    
    def getColor(self):
        return self.color  # get vehicle
    
    def __str__(self):
        return f"This vehicle is {self.color}"  # Description of the vehicle

class Car(Vehicle): #inheritance
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color) 
        self.has_winter_tires = has_winter_tires  # Boolean 
    
    def __str__(self):
        return super().__str__() + f"\nHas winter tires: {self.has_winter_tires}"


class Truck(Vehicle): # inheritance
    def __init__(self, color, has_trailer=False):
        super().__init__(color)  # Initialize 
        self.has_trailer = has_trailer  # Boolean for trailer
    
    def __str__(self):
        return super().__str__() + f"\nHas trailer: {self.has_trailer}"

class Garage:
    def __init__(self):
        self.parked_vehicle = None  # No vehicle parked initially
    
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
        truck = Truck("black", has_trailer=False)  # Create a black truck with no trailer
        garage = Garage()  # Create a garage
        garage.setVehicle(truck)  # Park the truck in the garage
        print(garage)  # Print garage details


# Customer Class
class Customer:
    def __init__(self, name, address):
        self.name = name  # Store the customer's name
        self.address = address  # Store the customer's address
    
    def __str__(self):
        return f"Customer Name: {self.name}, Address: {self.address}"


# Example usage
if __name__ == "__main__":
    GarageTester.getExample()  # Test the garage system

    customer = Customer("John Doe", "123 Elm Street")  # Create a customer
    print(customer)  # Print customer details
