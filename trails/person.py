class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
person1 = Person("luqman", 25)
person1.display_info()
person2 = Person("kyembe", 30)
person2.display_info()
person3 = Person("Bob", 40)
person3.display_info()
        