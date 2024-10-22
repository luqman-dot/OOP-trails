class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
    
    def get_area(self):
        return 3.14 * self.radius**2
    
class Square(Shape):
    def __init__(self, color, filled, side_length):
        super().__init__(color, filled)
        self.side_length = side_length
        
    def get_area(self):
        return self.side_length**2 
    
class Rectangle(Shape):
    def __init__(self, color, filled, side_length, height):
        super().__init__(color, filled)
        self.side_length = side_length
        self.height = height
        
    def get_area(self):
        return self.side_length * self.height
    
    
circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=True, side_length=20)
Rectangle = Rectangle(color="yellow", filled=True, side_length=3, height=6)

print("Circle Area:", circle.get_area(),"cm²")
print("Square Area:", square.get_area(),"cm²")
print("Rectangle:", square.get_area(),"cm²")
