from oop.decorators_exercise.computer_store.computer_types.desktop_computer import DesktopComputer
from oop.decorators_exercise.computer_store.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTERS = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse = []  # Computers Obj List
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if not type_computer in self.VALID_COMPUTERS.keys():
            raise ValueError(f"{type_computer} is not a valid type computer!")

        self.warehouse.append(self.VALID_COMPUTERS[type_computer](manufacturer, model))
        return self.warehouse[-1].configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        searched_computer = None
        for device in self.warehouse:
            if device.price <= client_budget and device.processor == wanted_processor and device.ram >= wanted_ram:
                searched_computer = device
                # Removing it from warehouse
                self.warehouse.remove(device)
                break

        if not searched_computer:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - searched_computer.price
        return f"{searched_computer} sold for {client_budget}$."
