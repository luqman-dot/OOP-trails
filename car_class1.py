class Car:
    def __init__(self, make, model, fuel_capacity, fuel_efficiency):
        self.make = make
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_efficiency = fuel_efficiency
        self.current_fuel = fuel_capacity
        self.speed = 0  # km/h
        self.distance_traveled = 0  # kilometers

    def accelerate(self, increase):
        """Increase the car's speed."""
        if increase <= 0:
            print("Speed increase must be positive!")
            return
        self.speed += increase
        print(f"The car accelerates. Current speed: {self.speed} km/h")

    def brake(self, decrease):
        """Decrease the car's speed."""
        if decrease <= 0:
            print("Speed decrease must be positive!")
            return
        self.speed = max(0, self.speed - decrease)
        print(f"The car slows down. Current speed: {self.speed} km/h")

    def drive(self, hours):
       
        if self.speed == 0:
            print("The car is stationary. Accelerate to start driving.")
            return

        if hours <= 0:
            print("Driving time must be positive!")
            return

        distance = self.speed * hours
        fuel_needed = distance / self.fuel_efficiency

        if fuel_needed > self.current_fuel:
            max_distance = self.current_fuel * self.fuel_efficiency
            self.distance_traveled += max_distance
            self.current_fuel = 0
            print(f"Out of fuel after driving {max_distance:.2f} km.")
        else:
            self.distance_traveled += distance
            self.current_fuel -= fuel_needed
            print(f"You drove {distance:.2f} km and used {fuel_needed:.2f} liters of fuel.")

    def refuel(self, liters):
        
        if liters <= 0:
            print("Fuel amount must be positive!")
            return

        if self.current_fuel + liters > self.fuel_capacity:
            added = self.fuel_capacity - self.current_fuel
            self.current_fuel = self.fuel_capacity
            print(f"Fuel tank is full! Added {added:.2f} liters.")
        else:
            self.current_fuel += liters
            print(f"Added {liters:.2f} liters of fuel. Current fuel: {self.current_fuel:.2f} liters.")

    def display_status(self):
        """Show the current status of the car."""
        fuel_warning = " (LOW FUEL!)" if self.current_fuel < 5 else ""
        print(f"""
        Car: {self.make} {self.model}
        Fuel: {self.current_fuel:.2f}/{self.fuel_capacity} liters{fuel_warning}
        Distance Traveled: {self.distance_traveled:.2f} km
        Current Speed: {self.speed} km/h
        """)

# Improved Menu-Based Interaction
def car_simulator():
    car = Car("Tesla", "Model S", 75, 20)

    while True:
        print("\nWhat would you like to do?")
        print("1. Accelerate")
        print("2. Brake")
        print("3. Drive")
        print("4. Refuel")
        print("5. Check Status")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                amount = int(input("Enter speed to increase (km/h): "))
                car.accelerate(amount)

            elif choice == "2":
                amount = int(input("Enter speed to decrease (km/h): "))
                car.brake(amount)

            elif choice == "3":
                hours = float(input("Enter hours to drive: "))
                car.drive(hours)

            elif choice == "4":
                liters = float(input("Enter liters of fuel to add: "))
                car.refuel(liters)

            elif choice == "5":
                car.display_status()

            elif choice == "6":
                print("Exiting simulation. Drive safe!")
                break

            else:
                print("Invalid choice. Please choose a valid option.")

        except ValueError:
            print("Invalid input! Please enter numeric values where required.")

if __name__ == "__main__":
    car_simulator()
