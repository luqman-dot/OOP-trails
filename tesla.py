class Car:
    def __init__ (self, brand ,model, year):
        self.brand= brand
        self._model= model
        self.__year= year 
        
    def get_brand(self):
        return self.brand
    def get_model(self):
        return self._model
    def get__year(self):
        return self.__year
    def set__year(self, year):      
        self.__year= year
        
car1= Car("ferrari ", "california", 2002)
car1.set__year(2024)
print(car1.brand)
print(car1._model)
print(car1.get__year()
