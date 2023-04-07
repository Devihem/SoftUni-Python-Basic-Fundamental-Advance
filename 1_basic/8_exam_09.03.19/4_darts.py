player_name = input()
points = 301
multiplier = 0
true_shots = 0
fail_shots = 0

while True:
    command = input()
    if command == "Retire":
        print(f"{player_name} retired after {fail_shots} unsuccessful shots.")
        break
    elif command == "Single":
        multiplier = 1
    elif command == "Double":
        multiplier = 2
    elif command == "Triple":
        multiplier = 3

    score = int(input())
    active_score = score * multiplier

    if points - active_score < 0:
        fail_shots += 1
        continue
    elif points - active_score > 0:
        points -= active_score
        true_shots += 1
    elif points - active_score == 0:
        true_shots += 1
        print(f"{player_name} won the leg with {true_shots} shots.")
        break
