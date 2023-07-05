from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        # If place  bla bla  = MOney +
        # Petronas
        # 1st place – 1 000 000$
        # 3nd place – 500 000$
        # TeamViewer
        # 5th place – 100 000$
        # 7th place – 50 000$
        #
        #  minus tezi pari
        # Exp Per Race 200k
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
