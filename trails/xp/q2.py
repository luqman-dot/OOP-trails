class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, tank_capacity):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.tank_capacity = tank_capacity  
        self.fuel_level = 0  

    def refuel(self, amount):
        if self.fuel_level + amount > self.tank_capacity:
            print(f"Cannot add {amount} liters. Tank can only hold {self.tank_capacity - self.fuel_level} more liters.")
            self.fuel_level = self.tank_capacity  
        else:
            self.fuel_level += amount
            print(f"Added {amount} liters of fuel. Current fuel level: {self.fuel_level} liters.")

    def drive(self, distance):
        fuel_needed = distance / 10  
        if fuel_needed > self.fuel_level:
            print(f"Not enough fuel to drive {distance} km. Refuel first!")
        else:
            self.fuel_level -= fuel_needed
            print(f"Successfully drove {distance} km. Remaining fuel: {self.fuel_level} liters.")

    def display_vehicle_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Fuel Level: {self.fuel_level} liters")
        print(f"Tank Capacity: {self.tank_capacity} liters")

my_car = Car("Toyota", "Corolla", 2022, "Petrol", 50)

# Simulate driving and refueling
my_car.display_vehicle_info()
print()  # Blank line for readability

my_car.refuel(20)  # Add 20 liters of fuel
my_car.drive(150)  # Drive 150 km
my_car.refuel(40)  # Try to add 40 liters (exceeds capacity)
print()  # Blank line for readability

# Display car information again
my_car.display_vehicle_info()
