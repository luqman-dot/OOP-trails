class Student:
    def __init__(self) -> None:
        self.name = ""
        self.age = 0
        self.year = ""
        self.RegNo = ""  
        
    def input_info(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.year = int(input("Enter your year: "))
        self.RegNo = input("Enter your registration NO: ")
        
    def display_info(self):
        # print(f"Student name: {self.name}, Age: {self.age}, Year: {self.year}, Registration No: {self.RegNo}")
        print(f"{self.name} is {self.age} years old and is in year {self.year} with Registration No: {self.RegNo}")
    
student1 = Student()
student1.input_info()  
student1.display_info()
