import re

players_list = input().split(", ")
players_dict = {name: 0 for name in players_list}

while True:
    command = input()
    if command == "end of race":
        break

    player_name = re.findall(r"[a-zA-Z]+", command)
    player_distance = re.findall(r"\d", command)
    player_name_str = "".join(player_name)
    player_distance_sum = sum(map(int, player_distance))
    if player_name_str in players_list:
        players_dict[player_name_str] = players_dict[player_name_str] + player_distance_sum

racers_position = sorted(players_dict.items(), key=lambda k: (k[1], k[0]), reverse=True)
print(f"1st place: {racers_position[0][0]}\n\
2nd place: {racers_position[1][0]}\n\
3rd place: {racers_position[2][0]}")
