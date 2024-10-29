class Camera:
    def take_photo(self):
        print("Taking a photo.....captured")

class Phone:
    def making_call(self):
        print("Making a call...")
        
class Ring:
    def ringing(self):
        print("ringing................................")

class Smartphone(Camera, Phone, Ring):
    pass

smartphone = Smartphone()
smartphone.take_photo()
smartphone.making_call()
smartphone.ringing()
