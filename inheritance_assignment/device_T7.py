class Device: #parent
    def info(self):
        print("Device information")

# inherits from Device
class Computer(Device):
    def info(self):
        super().info()
        print("Computer information")

# inherits from Computer
class Laptop(Computer):
    def info(self):
        super().info()
        print("Laptop information")

laptop = Laptop()
laptop.info()
