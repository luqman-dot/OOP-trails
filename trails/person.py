class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
# person1 = Person("luqman", 25)
# person1.display_info()

class Student(Person):
    def __init__(self, name, age, grade):
        print(f"{self.name} {self.age} {self.grade}")


                