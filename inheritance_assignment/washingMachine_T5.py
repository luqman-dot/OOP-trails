class Appliance:  #parent_class
    def __init__(self, brand, power, capacity):
        self.brand = brand
        self.power = power
        self.capacity = capacity

# WashingMachine Class_Child
class WashingMachine(Appliance):
    def __init__(self, brand, power, capacity, drum_size):
        super().__init__(brand, power,capacity)
        self.drum_size = drum_size

    def show_details(self):
        print(f"Brand: {self.brand}, Power: {self.power}W, capacity: {self.capacity}kgs, Drum Size: {self.drum_size}L")

washing_machine = WashingMachine("Samsung", 1500, 7, 55)
washing_machine.show_details()
