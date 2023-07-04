from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, drive_distance):
        pass

    @abstractmethod
    def refuel(self, refuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, drive_distance):
        ac_consumption = 0.9
        current_consumption = self.fuel_consumption + ac_consumption
        if self.fuel_quantity / current_consumption >= drive_distance:
            self.fuel_quantity -= drive_distance * current_consumption

    def refuel(self, refuel):
        self.fuel_quantity += refuel


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, drive_distance):
        ac_consumption = 1.6
        current_consumption = self.fuel_consumption + ac_consumption
        if self.fuel_quantity / current_consumption >= drive_distance:
            self.fuel_quantity -= drive_distance * current_consumption

    def refuel(self, refuel):
        self.fuel_quantity += refuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
