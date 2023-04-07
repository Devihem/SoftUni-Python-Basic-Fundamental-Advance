first_match_result = input()
second_match_result = input()
third_match_result = input()

won_games = 0
lost_games = 0
draw_games = 0

if int(first_match_result[0]) > int(first_match_result[2]):
    won_games += 1
elif int(first_match_result[0]) < int(first_match_result[2]):
    lost_games += 1
else:
    draw_games += 1

if int(second_match_result[0]) > int(second_match_result[2]):
    won_games += 1
elif int(second_match_result[0]) < int(second_match_result[2]):
    lost_games += 1
else:
    draw_games += 1

if int(third_match_result[0]) > int(third_match_result[2]):
    won_games += 1
elif int(third_match_result[0]) < int(third_match_result[2]):
    lost_games += 1
else:
    draw_games += 1

print(f"Team won {won_games} games.")
print(f"Team lost {lost_games} games.")
print(f"Drawn games: {draw_games}")