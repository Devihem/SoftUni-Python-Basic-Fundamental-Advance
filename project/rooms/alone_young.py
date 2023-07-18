from project.rooms.room import Room


class AloneYoung(Room):
    APPLIANCES_LIST = [Room.add_tv()]

    def __init__(self, family_name: str, salary: float):
        budget = salary
        members_count = 1
        super().__init__(family_name, budget, members_count)
        self.room_cost = 10
        self.__expenses = self.calculate_expenses(self.APPLIANCES_LIST * members_count, self.children)
