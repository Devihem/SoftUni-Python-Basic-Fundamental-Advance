from project.rooms.room import Room
from project.people.child import Child


class YoungCoupleWithChildren(Room):
    ROOM_COST = 30
    APPLIANCES_LIST = [Room.add_tv(), Room.add_laptop(), Room.add_fridge()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        budget = salary_one + salary_two
        members_count = 2 + len(children)
        super().__init__(family_name, budget, members_count)
        self.children = list(children)
        self.expenses = self.calculating_expenses_total(self.members_count, self.APPLIANCES_LIST, self.children)

