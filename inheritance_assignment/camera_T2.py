class Camera:
    def take_photo(self):
        print("Taking a photo...")

class Phone:
    def beep_call(self):
        print("Beep call...")

class Smartphone(Camera, Phone):
    pass

smartphone = Smartphone()
smartphone.take_photo()
smartphone.beep_call()
