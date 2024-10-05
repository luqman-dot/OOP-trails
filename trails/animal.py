class animal:
    def __init__(self,name):
        self.name = name
        self.is alive = True
        
def eat (self):
    print(f"self.name" is eating)
    
def sleep (self):
    print(f"self.name" is sleeping)
    
class dog (animal):
    pass

class cat (animal):
    pass

dog = dog("self.name")
cat = cat("self.name")

print(cat.name)