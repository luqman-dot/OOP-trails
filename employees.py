class Employees:
    def __init__ (self ,name, age):
        self.name = name 
        self.age = age
        
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
Emp1 = Employees("luqman kyembe", "20")
Emp2 = Employees("josh babes", "20")

Emp1.display_details()        