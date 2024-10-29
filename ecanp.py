# base=100000
# overtime=40
# rate=250000

# def get_wage(base_salary,overtime,rate):
#     return base_salary + (overtime)

# salary = get_wage(base_salary,overtime,rate)

# base_salary = 100000
# overtime = 5
# rate1 = 250000

class Employee:
    def __init__(self, base_salary, overtime, rate):
        self.base_salary = base_salary
        self.overtime = overtime
        self.rate = rate

    def get_wage(self):
        return self.base_salary + (self.overtime * self.rate)

employee1= Employee(base_salary=100000, overtime=5, rate=250000)

salary = employee1.get_wage()
print("Total Salary:", salary)
