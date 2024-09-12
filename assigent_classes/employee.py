class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Salary: Ugx {self.salary}")

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} has been given a raise of ${amount}. New salary is ${self.salary}.")


employee_1 = Employee("Luqman Kyembe", 101, "HR", 500000)
employee_1.display_info()

employee_1.give_raise(50000)
employee_1.display_info()
