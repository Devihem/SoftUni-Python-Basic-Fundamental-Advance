from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV


class Room:
    ROOM_COST = 0

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.room_cost = self.ROOM_COST
        self.children = []  # Obj list
        self.expenses = 0  # If it is set to a negative number, raise ValueError

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    # Helpers -------------------------------------------------------------------

    @staticmethod
    def add_tv():
        return TV()

    @staticmethod
    def add_fridge():
        return Fridge()

    @staticmethod
    def add_laptop():
        return Laptop()

    @staticmethod
    def add_stove():
        return Stove()

    @staticmethod
    def calculate_expenses(*args):
        return sum([unit.cost * 30 for unit in args])

    @staticmethod
    def calculating_expenses_total(members, appliances_list, children_list):
        return (Room.calculate_expenses(*appliances_list) * members) + Room.calculate_expenses(*children_list)
