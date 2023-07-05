from formula_teams.formula_team import FormulaTeam
from formula_teams.red_bull_team import RedBullTeam
from formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        valid_names = ["Red Bull", "Mercedes"]
        if team_name in valid_names:
            if team_name == valid_names[0]:
                self.red_bull_team = team_name
            elif team_name == valid_names[1]:
                self.mercedes_team = team_name

            return f"{team_name} has joined the new F1 season."

        else:
            raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            return "Not all teams have registered for the season."

        return f"Red Bull: { Red Bull revenue message }. " \
               f"Mercedes: { Mercedes revenue message }. " \
               f"{ team with better position } is ahead at the { race name } race."
