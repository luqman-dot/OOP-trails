from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def calculate_area(self):
        pass
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
shapes = [Circle(5), Triangle(6,7)]
for shape in shapes:
    print(f"Area: {shape.calculate_area()} cm²")
    