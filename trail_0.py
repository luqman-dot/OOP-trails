# class Variable
class Car: 
    def __init__(self, color, model, numberplate, year):
        
        # instance variable
        self.color = color
        self.model = model
        self.numberplate = numberplate
        self.year = year

car_1 = Car("yellow", "Mustang", 899, 2000)
car_2 = Car("green", "Lambo", 100, 2020)

print(car_1.model)
