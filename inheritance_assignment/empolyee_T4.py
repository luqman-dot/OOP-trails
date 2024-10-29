class Employee:     #parent class
    def work(self):
        print("Employee is working.")

# Manager Class_Child
class Manager(Employee):
    def work(self):
        print("Manager is managing the team.")

# Developer Class_Child
class Developer(Employee):
    def work(self):
        print("Developer is writing code.")

manager = Manager()
developer = Developer()
manager.work()
developer.work()
