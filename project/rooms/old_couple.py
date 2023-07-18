from project.rooms.room import Room


class OldCouple(Room):
    ROOM_COST = 15
    APPLIANCES_LIST = [Room.add_tv(), Room.add_stove(), Room.add_fridge()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        budget = pension_one + pension_two
        members_count = 2
        super().__init__(family_name, budget, members_count)
        self.expenses = self.calculating_expenses_total(self.members_count, self.APPLIANCES_LIST, self.children)
