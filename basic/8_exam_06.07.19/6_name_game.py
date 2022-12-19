total_points = 0
leading_name = ""
best_result = 0

while True:
    player_name = input()
    if player_name == "Stop":
        break
    for i in range(0, len(player_name)):
        guess_number = int(input())
        if chr(guess_number) == repr(player_name)[1+i]:
            total_points += 10
        else:
            total_points += 2
        if best_result <= total_points:
            leading_name = player_name
            best_result = total_points
    total_points = 0
print(f"The winner is {leading_name} with {best_result} points!")
