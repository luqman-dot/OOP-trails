class Vehicle:
    def __init__(self, model):
        self.model = model
        
    def race(self):
        print("Start your engine!!!!")

class Car(Vehicle):
    def __init__(self, model, number_of_doors):
        super().__init__(model)
        self.number_of_doors = number_of_doors

class Electric_Car(Car):
    def __init__(self, model, number_of_doors, battery_capacity):
        super().__init__(model, number_of_doors)
        self.battery_capacity = battery_capacity

    def show_details(self):
        print(f"Type: {self.model}, Doors: {self.number_of_doors}, Battery: {self.battery_capacity}kWh")
        
car = Electric_Car("Posh 911 california", 2, 75)
car.race()
car.show_details()
 