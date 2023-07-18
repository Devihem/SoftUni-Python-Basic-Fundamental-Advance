from project.rooms.room import Room


class YoungCouple(Room):
    APPLIANCES_LIST = [Room.add_tv(), Room.add_laptop(), Room.add_fridge()]

    def __init__(self, family_name: str, salary_one, salary_two):
        budget = salary_one + salary_two
        members_count = 2
        super().__init__(family_name, budget, members_count)
        self.room_cost = 20
        self.__expenses = self.calculate_expenses(self.APPLIANCES_LIST * members_count, self.children)
