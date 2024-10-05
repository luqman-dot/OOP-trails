# class Variable
class Car: 
    def __init__(self, color, model, numberplate, year):
        
        self.color = color  # instance variable
        self.model = model  # instance variable
        self.numberplate = numberplate  # instance variable
        self.year = year
        
    def display_info(self):
        print(f"car: {self.color} {self.model} {self.numberplate} {self.year}")    

car_1 = Car("yellow", "Mustang", 899, 2000)
car_2 = Car("green", "Lambo", 100, 2020)

print(car_1.display_info())

