class Uni:
    def __init__(self, name , location, email):
        self.name = name
        self.location = location
        self.email = email
        
def info(self):
    print(f"you are a student of {self.name} located at {self.location} and this is your email {self.email}")
    
uni1 = Uni("UCU" , "Mukono", "ucu@gmail.com",)

print(info(uni1))
        