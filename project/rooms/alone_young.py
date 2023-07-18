from project.rooms.room import Room


class AloneYoung(Room):
    ROOM_COST = 10
    APPLIANCES_LIST = [Room.add_tv()]

    def __init__(self, family_name: str, salary: float):
        budget = salary
        members_count = 1
        super().__init__(family_name, budget, members_count)
        self.expenses = self.calculating_expenses_total(self.members_count, self.APPLIANCES_LIST, self.children)
