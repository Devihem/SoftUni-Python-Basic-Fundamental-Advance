from project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name: str):
        super().__init__(name, 15)
        self.type = 'Drink'

    def details(self):
        return f"{self.type}: {self.name}, {self.energy}"

