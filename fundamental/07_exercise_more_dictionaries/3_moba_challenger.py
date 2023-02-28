def player_structure_dict(name: str, role: str, score: int, players_info_dict: dict):
    if name not in players_info_dict:
        players_info_dict[name] = {}
    if role not in players_info_dict[name]:
        players_info_dict[name][role] = 0
    if score > players_info_dict[name][role]:
        players_info_dict[name][role] = score
    return players_info_dict


def player_versus(first_player: str, second_player: str, players_info_dict: dict):
    if first_player in players_info_dict and second_player in players_info_dict:

        if players_info_dict[first_player].items == players_info_dict[second_player].items:
            # 1 if both players have the same roles and same points for them [key].items == [key].items
            pass
        else:
            same_positions = 0
            for role in (players_info_dict[first_player].keys()):
                if role in players_info_dict[second_player].keys():
                    same_positions += 1
            if same_positions > 0:
                # 2 if at-least one position is same in both players dict
                first_player_total_score = sum(players_info_dict[first_player].values())
                second_player_total_score = sum(players_info_dict[second_player].values())
                if first_player_total_score > second_player_total_score:
                    players_info_dict.pop(second_player)
                elif second_player_total_score > first_player_total_score:
                    players_info_dict.pop(first_player)
            else:
                # 3 of players don't have position in common [key] not in [key]
                pass
    return players_info_dict


players_dict = {}

while True:
    new_input = input()
    if new_input == "Season end":
        break
    elif "->" in new_input:
        player, position, point = new_input.split(" -> ")
        players_dict = player_structure_dict(player, position, int(point), players_dict)
    else:
        player_one, player_two = new_input.split(" vs ")
        players_dict = player_versus(player_one, player_two, players_dict)

sorted_max_score_dict = {}
for player_x in players_dict:
    sorted_max_score_dict[player_x] = sum(players_dict[player_x].values())


sorted_max_score_names = sorted(sorted_max_score_dict.items(), key=lambda k: (-k[1], k[0]))

for final_print_player, final_sum_score in sorted_max_score_names:
    print(f"{final_print_player}: {final_sum_score} skill")
    player_roles_printable_version = sorted(players_dict[final_print_player].items(), key=lambda k: (-k[1], k[0]))
    for final_key, final_key_score in player_roles_printable_version:
        print(f"- {final_key} <::> {final_key_score}")
