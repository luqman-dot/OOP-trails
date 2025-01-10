class Car:
    def __init__(self, make, model, fuel_capacity, fuel_efficiency):
        """
        Initialize the car with basic attributes.
        :param make: Manufacturer of the car
        :param model: Model name of the car
        :param fuel_capacity: Maximum fuel tank capacity in liters
        :param fuel_efficiency: Fuel efficiency in kilometers per liter
        """
        self.make = make
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_efficiency = fuel_efficiency
        self.current_fuel = fuel_capacity
        self.speed = 0  # km/h
        self.distance_traveled = 0  # kilometers

    def accelerate(self, increase):
        """Increase the car's speed."""
        self.speed += increase
        print(f"The car accelerates. Current speed: {self.speed} km/h")

    def brake(self, decrease):
        """Decrease the car's speed."""
        self.speed = max(0, self.speed - decrease)
        print(f"The car slows down. Current speed: {self.speed} km/h")

    def drive(self, hours):
        """
        Simulate driving the car for a certain number of hours.
        :param hours: Time to drive in hours
        """
        if self.speed == 0:
            print("The car is stationary. Accelerate to start driving.")
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
        """
        Refuel the car's tank.
        :param liters: Amount of fuel to add in liters
        """
        if self.current_fuel + liters > self.fuel_capacity:
            print(f"Fuel tank is full! Can only add {self.fuel_capacity - self.current_fuel:.2f} liters.")
            self.current_fuel = self.fuel_capacity
        else:
            self.current_fuel += liters
            print(f"Added {liters:.2f} liters of fuel. Current fuel: {self.current_fuel:.2f} liters.")

    def display_status(self):
        """Show the current status of the car."""
        print(f"""
        Car: {self.make} {self.model}
        Fuel: {self.current_fuel:.2f}/{self.fuel_capacity} liters
        Distance Traveled: {self.distance_traveled:.2f} km
        Current Speed: {self.speed} km/h
        """)


# Example Usage
if __name__ == "__main__":
    my_car = Car("Tesla", "Model 3", 50, 20)

    # Car simulation
    my_car.display_status()
    my_car.accelerate(60)
    my_car.drive(2)
    my_car.brake(20)
    my_car.refuel(10)
    my_car.drive(1)
    my_car.display_status()
