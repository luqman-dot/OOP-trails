from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    
    def stop(self):
        pass
    
class Car(Vehicle):
    def go(self):
        print("you can go")
        
    def stop(self):
        print("you can stop")
        
car1 = Car()
car1.go() 
    