class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades 

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

# Example usage
student = Student("Alice", 16, [85, 90, 78, 92])
print(f"Name: {student.name}, Age: {student.age}, GPA: {student.calculate_gpa():.2f}")
