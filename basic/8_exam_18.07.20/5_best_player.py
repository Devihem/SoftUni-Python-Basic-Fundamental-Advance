
best_player = ""
best_goals_score = 0

while True:
    player_name = input()
    if player_name == "END":
        break
    goals = int(input())
    if best_goals_score < goals:
        best_goals_score = goals
        best_player = player_name
    if goals >= 10:
        break

print(f"{best_player} is the best player!")

if best_goals_score >= 3:
    print(f"He has scored {best_goals_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals_score} goals.")