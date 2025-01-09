import time

class Car:
    def __init__(self, make, model, fuel_capacity, fuel_efficiency):
        self.make = make
        self.model = model
        self.fuel_capacity = fuel_capacity  # in liters
        self.fuel_efficiency = fuel_efficiency  # kilometers per liter
        self.current_fuel = fuel_capacity
        self.speed = 0  # in km/h
        self.distance_traveled = 0  # in km

    def accelerate(self, increase):
        self.speed += increase
        print(f"You accelerated. Current speed: {self.speed} km/h")

    def brake(self, decrease):
        self.speed = max(0, self.speed - decrease)
        print(f"You slowed down. Current speed: {self.speed} km/h")

    def drive(self, time_in_hours):
        if self.speed == 0:
            print("The car is not moving. Accelerate to drive.")
            return

        distance = self.speed * time_in_hours
        fuel_needed = distance / self.fuel_efficiency

        if fuel_needed > self.current_fuel:
            max_distance = self.current_fuel * self.fuel_efficiency
            self.distance_traveled += max_distance
            self.current_fuel = 0
            print(f"You ran out of fuel after driving {max_distance:.2f} km.")
        else:
            self.distance_traveled += distance
            self.current_fuel -= fuel_needed
            print(f"You drove {distance:.2f} km.")

    def refuel(self, amount):
        if self.current_fuel + amount > self.fuel_capacity:
            print(f"Fuel tank is full. You can only add {self.fuel_capacity - self.current_fuel:.2f} liters.")
            self.current_fuel = self.fuel_capacity
        else:
            self.current_fuel += amount
            print(f"You added {amount:.2f} liters of fuel. Current fuel: {self.current_fuel:.2f} liters.")

    def status(self):
        print(f"""
        Car: {self.make} {self.model}
        Fuel: {self.current_fuel:.2f}/{self.fuel_capacity} liters
        Distance Traveled: {self.distance_traveled:.2f} km
        Current Speed: {self.speed} km/h
        """)

def main():
    car = Car("Toyota", "Corolla", 50, 15)  # Example car with 50 liters tank and 15 km/l efficiency

    while True:
        print("\nCar Driving Simulator")
        print("1. Accelerate")
        print("2. Brake")
        print("3. Drive")
        print("4. Refuel")
        print("5. Check Status")
        print("6. Exit")
        choice = input("Choose an action: ")

        if choice == "1":
            amount = int(input("Enter the speed increase (km/h): "))
            car.accelerate(amount)

        elif choice == "2":
            amount = int(input("Enter the speed decrease (km/h): "))
            car.brake(amount)

        elif choice == "3":
            time_in_hours = float(input("Enter the time to drive (in hours): "))
            car.drive(time_in_hours)

        elif choice == "4":
            amount = float(input("Enter the amount of fuel to add (liters): "))
            car.refuel(amount)

        elif choice == "5":
            car.status()

        elif choice == "6":
            print("Exiting the simulator. Drive safe!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
