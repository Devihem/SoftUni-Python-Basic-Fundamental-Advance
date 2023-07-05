from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int, ):
        self.__budget = budget

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        pass

    @property
    def budget(self):
        return __budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value
