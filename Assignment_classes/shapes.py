class Shape:
    shape_type = "Geometric Shape"  # Class variable

    def __init__(self, name, size):
        self.name = name  # Instance variable
        self.size = size  # Instance variable

    @classmethod
    def get_shape_type(cls):
        return cls.shape_type  # Class method accessing class variable

    @staticmethod
    def description():
        return "Shapes have different sizes and areas."  # Static method, no class or instance reference

    def area(self):
        if self.name.lower() == "circle":
            return 3.14 * (self.size ** 2)  
        elif self.name.lower() == "square":
            return self.size ** 2  
        else:
            return "Unknown shape"

circle = Shape("Circle", 5)
square = Shape("Square", 4)

print(Shape.get_shape_type())         
print(Shape.description())            
print(circle.area())                  
print(square.area())                  
