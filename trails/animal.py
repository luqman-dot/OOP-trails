class animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
        
    def eat (self):
        print(f"{self.name} is eating")
    
    def sleep (self):
        print(f"{self.name} is sleeping")
    
class Dog(animal):
    pass

class Cat(animal):
    pass

dog = Dog("scooby max")
cat = Cat("gafield")

# print(cat.name)
dog.sleep()
dog.eat()
cat.eat()