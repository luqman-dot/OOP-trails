class Vehicle:
    def __init__(self, model):
        self.model = model

    def race(self):
        print("Start your engine!!!!")

class Car(Vehicle):
    def __init__(self, model, number_of_doors):
        super().__init__(model)
        self.number_of_doors = number_of_doors


class Sunroof:
    def __init__(self, has_sunroof):
        self.has_sunroof = has_sunroof


class Horsepower:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Electric_Car(Car, Sunroof, Horsepower):
    def __init__(self, model, number_of_doors, battery_capacity, has_sunroof, horsepower):
        Car.__init__(self, model, number_of_doors)
        Sunroof.__init__(self, has_sunroof)
        Horsepower.__init__(self, horsepower)
        self.battery_capacity = battery_capacity

    def show_details(self):
        sunroof_status = "Yes" if self.has_sunroof else "No"
        print(f"Model: {self.model}, Doors: {self.number_of_doors}, "
              f"Battery: {self.battery_capacity}kWh, Sunroof: {sunroof_status}, "
              f"Horsepower: {self.horsepower} HP")

car = Electric_Car("Posh 911 California", 2, 75, has_sunroof=True, horsepower=350)
car.race()
car.show_details()
