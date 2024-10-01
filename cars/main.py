class BSIT_2:
    def __init__(self, name, age, regNO, student_ID):
        self.name = name
        self.age = age
        self.regNO = regNO
        self.student_ID = student_ID

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, regNO: {self.regNO}, Student ID: {self.student_ID}"

    def update_student_ID(self, new_student_ID):
        self.student_ID = new_student_ID
        return f"{self.name}'s student ID has been updated to {self.student_ID}."

student1 = BSIT_2("josh babes", 20, "BSIT2 024001", "S12345")
print(student1.get_details())

print(student1.update_student_ID("S54321"))
