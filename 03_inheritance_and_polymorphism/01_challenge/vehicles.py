from abc import ABC, abstractmethod

# 抽象基底クラス
class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def get_details(self):
        pass

# Car クラス
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def get_details(self):
        return f"Car: {self.year} {self.make} {self.model}"

# Truck クラス
class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_details(self):
        return f"Truck: {self.year} {self.make} {self.model}, Towing Capacity: {self.towing_capacity}"

# display_vehicle_details 関数
def display_vehicle_details(vehicle):
    if not isinstance(vehicle, Vehicle):
        raise TypeError("Expected an instance of Vehicle or its subclass")
    print(vehicle.get_details())