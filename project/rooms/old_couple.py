from project.rooms.room import Room


class OldCouple(Room):
    APPLIANCES_LIST = [Room.add_tv(), Room.add_stove(), Room.add_fridge()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        budget = pension_one + pension_two
        members_count = 2
        super().__init__(family_name, budget, members_count)
        self.room_cost = 15
        self.__expenses = self.calculate_expenses(self.APPLIANCES_LIST * members_count, self.children)
