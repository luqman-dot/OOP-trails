class Student:
    total_students = 0

    def __init__(self) -> None:
        self.name = ""
        self.age = 0
        self.year = ""
        self.RegNo = ""
        Student.total_students += 1

    def input_info(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.year = int(input("Enter your year: "))
        self.RegNo = input("Enter your registration NO: ")

    def display_info(self):
        print(f"{self.name} is {self.age} years old and is in year {self.year} with Registration No: {self.RegNo}")

    @classmethod
    def display_total_students(cls):
        print(f"Total number of students: {cls.total_students}")
    
student1 = Student()
student1.input_info()
student1.display_info()

student2 = Student()
student2.input_info()
student2.display_info()

Student.display_total_students()
