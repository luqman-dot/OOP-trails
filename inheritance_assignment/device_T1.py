class Device:
    def __init__(self, brand, model,):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_type):
        super().__init__(brand, model)
        self.storage = storage
        self.camera_type = camera_type

    def show_info(self):
        super().show_info()
        print(f"Storage_capacity: {self.storage} GB , camera_type: {self.camera_type}")

phone = Smartphone("Samsung", "S23", 128, "CCD")
phone.show_info()
