# more on method 
# starting with 2
class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show_info(self):
        print(f"Fruit: {self.name}, Color: {self.color}")

    def is_ripe(self):
        ripe_fruits = ["banana", "apple", "mango"]
        return self.name.lower() in ripe_fruits


fruit1 = Fruits("Apple", "Red")
fruit1.show_info()
print(f"Is the fruit ripe? {fruit1.is_ripe()}")


# 3 methods
