from abc import ABC, abstractmethod

class CarService(ABC):
    @abstractmethod
    def perform_service(self):
        pass

    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def service_duration(self):
        pass

    def generate_service_report(self):
        print("Service report: You car has been successfully worked upon.")


class Oil_change(CarService):
    def perform_service(self):
        print("Performing oil change.")

    def calculate_cost(self):
        return 3000000

    def service_duration(self):
        return "2 hours" 

class Tire_rotation(CarService):
    def perform_service(self):
        print("Rotating tires.")

    def calculate_cost(self):
        return 40  

    def service_duration(self):
        return "45 minutes" 

oil_change = Oil_change()
oil_change.perform_service()
print(f"Cost: Ugx {oil_change.calculate_cost()}")
print(f"Duration: {oil_change.service_duration()}")
oil_change.generate_service_report()
