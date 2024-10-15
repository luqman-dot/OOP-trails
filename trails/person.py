class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
# person1 = Person(name= "luqman", age= "20")
# person1.display_info()

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def display_info(self):
        super().display_info()
        print(f"Grade: {self.grade}")
        
class Lecturer(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

student = Student(name="Luqman", age=20, grade="G1")
lecturer = Lecturer(name="Bosco", age=20, department="Computing")

lecturer.display_info()
student.display_info()
