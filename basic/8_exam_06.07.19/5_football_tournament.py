team_name = input()
matches_played_loop = int(input())
final_result = 0
w_counter = 0
d_counter = 0
l_counter = 0

for i in range(0, matches_played_loop):
    match_result = input()

    if match_result == "W":
        final_result += 3
        w_counter += 1
    elif match_result == "D":
        final_result += 1
        d_counter += 1
    elif match_result == "L":
        l_counter += 1

if matches_played_loop < 1:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f"{team_name} has won {final_result} points during this season.")
    print("Total stats:")
    print(f"## W: {w_counter}")
    print(f"## D: {d_counter}")
    print(f"## L: {l_counter}")
    print(f"Win rate: {w_counter/matches_played_loop*100:.2f}%")
