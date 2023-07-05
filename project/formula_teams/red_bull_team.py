from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        # If place  bla bla  = MOney +
        # Oracle
        # 1st place – 1 500 000$
        # 2nd place – 800 000$
        # Honda
        # 8th place – 20 000$
        # 10th place – 10 000$
        #
        #  minus tezi pari
        # Exp Per Race 250k
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
