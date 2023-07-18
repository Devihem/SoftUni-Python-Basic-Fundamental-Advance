from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.laptop import Laptop


class YoungCouple(Room):
    ROOM_COST = 20
    APPLIANCES_LIST = [Room.add_tv(), Room.add_laptop(), Room.add_fridge()]

    def __init__(self, family_name: str, salary_one, salary_two):
        budget = salary_one + salary_two
        members_count = 2
        super().__init__(family_name, budget, members_count)
        self.expenses = self.calculate_expenses(*self.APPLIANCES_LIST) * self.members_count
