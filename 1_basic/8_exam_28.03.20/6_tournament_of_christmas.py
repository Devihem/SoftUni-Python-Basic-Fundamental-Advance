game_name = ""
current_day = 0
total_days = int(input())
money = 0
win_counter = 0
lose_counter = 0
total_money = 0
days_win_counter = 0

while current_day < total_days:
    game_name = input()

    if game_name == "Finish":
        if lose_counter < win_counter:
            money = money * 1.1
            days_win_counter += 1
        total_money += money
        money = 0
        win_counter = 0
        lose_counter = 0
        current_day += 1

    if game_name == "win":
        money += 20
        win_counter += 1
    elif game_name == "lose":
        lose_counter += 1

if total_days/2 < days_win_counter:
    total_money = total_money * 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")




