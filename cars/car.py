class Car:
    total_cars = 0    #class variable  

    def __init__(self, color, model , numberplate, year):
        self.color = color  # instance variable
        self.model = model  # instance variable
        self.numberplate = numberplate  # instance variable
        self.year = year

        Car.total_cars += 1

    def display_info(self):
        print(f"Car: {self.color} {self.model} {self.numberplate} {self.year}")

    @classmethod
    def display_total_cars(cls):
        print(f"Total number of cars: {cls.total_cars}")

car_1 = Car("yellow", "Mustang", 899, 2000)
car_2 = Car("green", "Lambo", 100, 2020)

car_1.display_info()
car_2.display_info()

Car.display_total_cars()
