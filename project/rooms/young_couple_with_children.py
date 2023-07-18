from project.rooms.room import Room
from project.people.child import Child


class YoungCoupleWithChildren(Room):
    APPLIANCES_LIST = [Room.add_tv(), Room.add_laptop(), Room.add_fridge()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        budget = salary_one + salary_two
        members_count = 2 + len(children)
        super().__init__(family_name, budget, members_count)
        self.children = list(children)
        self.room_cost = 30
        self.__expenses = self.calculate_expenses(self.APPLIANCES_LIST * members_count, self.children)


child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
