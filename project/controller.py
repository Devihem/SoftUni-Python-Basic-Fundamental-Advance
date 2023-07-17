from project.player import Player
from project.supply.food import Food
from project.supply.drink import Drink
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        currently_added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                currently_added_players.append(player.name)
        else:
            return f"Successfully added: {', '.join(currently_added_players)}"

    def add_supply(self, *supplies: Supply):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        searched_player = self.searching_player_by_name(player_name)

        # Check-1 - If there is no player - Ignore ! & Check-2 - If there is other supply type - Ignore !
        if searched_player and sustenance_type in ['Food', 'Drink']:
            if not searched_player.need_sustenance:  # Check-3 - If player don't need sustenance - Return msg
                return f"{searched_player.name} have enough stamina."

            searched_supply = self.searching_supply_by_type_reverse(sustenance_type)

            # Check-4 - If there is no more supply from this Type
            if searched_supply is None:
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

            if searched_player.stamina + searched_supply.energy > 100:
                searched_player.stamina = 100
            else:
                searched_player.stamina += searched_supply.energy

            return f"{searched_player.name} sustained successfully with {searched_supply.name}."

    # ########################---CHILL-LINE---#####################################################

    def duel(self, first_player_name: str, second_player_name: str):

        p1 = [player for player in self.players if first_player_name == player.name][0]
        p2 = [player for player in self.players if second_player_name == player.name][0]

        result = []

        if p1.stamina == 0 or p2.stamina == 0:
            if p1.stamina == 0:
                result.append(f"Player {p1.name} does not have enough stamina.")
            if p2.stamina == 0:
                result.append(f"Player {p2.name} does not have enough stamina.")
            return "\n".join(result)

        # Battle ! if work to implement a better script ?

        # Scenario 1  P1>P2
        if p1.stamina < p2.stamina:

            # P1 Attack
            attack_dmg_p1 = p1.stamina / 2
            if p2.stamina - attack_dmg_p1 <= 0:
                p2.stamina = 0
                return f"Winner: winner {p1.name}"
            else:
                p2.stamina -= attack_dmg_p1

            # P2 Attack
            attack_dmg_p2 = p2.stamina / 2
            if p1.stamina - attack_dmg_p2 <= 0:
                p1.stamina = 0
                return f"Winner: winner {p2.name}"
            else:
                p1.stamina -= attack_dmg_p2


        # Scenario 2 P2>P1
        elif p2.stamina < p1.stamina:

            # P2 - Attack
            attack_dmg_p2 = p2.stamina / 2
            if p1.stamina - attack_dmg_p2 <= 0:
                p1.stamina = 0
                return f"Winner: winner {p2.name}"
            else:
                p1.stamina -= attack_dmg_p2

            # P1 Attack
            attack_dmg_p1 = p1.stamina / 2
            if p2.stamina - attack_dmg_p1 <= 0:
                p2.stamina = 0
                return f"Winner: winner {p1.name}"
            else:
                p2.stamina -= attack_dmg_p1

        # Final Result  Winner
        winner = sorted([p1, p2], key=lambda k: k.stamina)[1]
        return f"Winner: winner {winner.name}"

    def next_day(self):
        for player in self.players:
            subtract_stamina = player.age * 2

            if player.stamina - subtract_stamina < 0:
                player.stamina = 0
            else:
                player.stamina -= subtract_stamina

        # Food and drink first or all Food first then all drink ?
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))
        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)

    # Helpers
    def searching_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def searching_supply_by_type_reverse(self, supply_type):
        for supply_index in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[supply_index].type == supply_type:
                return self.supplies.pop(supply_index)
