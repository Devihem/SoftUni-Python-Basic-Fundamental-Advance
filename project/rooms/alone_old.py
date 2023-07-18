from project.rooms.room import Room


class AloneOld(Room):
    ROOM_COST = 10
    APPLIANCES_LIST = []

    def __init__(self, family_name: str, pension: float):
        budget = pension
        members_count = 1
        super().__init__(family_name, budget, members_count)
        self.expenses = self.calculating_expenses_total(self.members_count, self.APPLIANCES_LIST, self.children)
