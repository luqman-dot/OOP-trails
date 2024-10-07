class Employee:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age if isinstance(age, int) and age > 0 else None
        if self.age is not None:
            raise ValueError("Age must be a positive integer.")
               
    def show_details(self) -> None:
        print(f"Employee details:\n name:(self.name)\n age:(self.age)\n")
        
emp1 = Employee("luqman shadow ", 20)
emp2 = Employee("josh kaven babes ",19)

emp1.show_details()
emp2.age.show_details()
    