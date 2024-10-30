class Animal:  #parent class
    def sound(self):
        print("animal sound")

# Dog Class_Child
class Frog(Animal):
    def sound(self):
        print(" Croaks and ribbit")

# Cat Class_Child
class Snake(Animal):
    def sound(self):
        print("FANTASTIC!!!!!!")

# Polymorphism func
def make_animal_sound(animal):
    animal.sound()

frog = Frog()
snake = Snake()
make_animal_sound(frog)
make_animal_sound(snake)
