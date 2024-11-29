
# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Define the Employee class, inheriting from Person
class Employee(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department
        self.tasks = []  

    # Method to assign a task
    def assign_task(self, task):
        if task not in self.tasks:  # Prevent assigning the same task twice
            self.tasks.append(task)
        else:
            print(f"Task '{task}' is already assigned to {self.name}.")

    # Method to display employee information
    def display_employee_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Tasks Assigned: {', '.join(self.tasks) if self.tasks else 'No tasks assigned'}")

# Create two employee objects
employee1 = Employee("Alice", 30, "Female", "E001", "IT")
employee2 = Employee("Bob", 28, "Male", "E002", "HR")

# Assign tasks to the employees
employee1.assign_task("Update Database")
employee1.assign_task("Create API")
employee1.assign_task("Update Database")  # Assigning duplicate task to test edge case

employee2.assign_task("Conduct Interviews")
employee2.assign_task("Review Policies")

# Display employee information
employee1.display_employee_info()
print()  # Add a blank line for better readability
employee2.display_employee_info()
