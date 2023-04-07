win_counter = 0
lost_counter = 0

while True:
    command = input()

    if command == "End of tournaments":
        print(f"{(win_counter / (win_counter + lost_counter)) * 100:.2f}% matches win")
        print(f"{(lost_counter / (win_counter + lost_counter)) * 100:.2f}% matches lost")
        break
    else:
        tournament_name = command

    number_of_matches = int(input())
    for m in range(1, number_of_matches+1):
        score_t1 = int(input())
        score_t2 = int(input())

        if score_t1 > score_t2:
            win_counter += 1
            print(f"Game {m} of tournament {tournament_name}: win with {score_t1 - score_t2} points.")
        elif score_t2 > score_t1:
            lost_counter += 1
            print(f"Game {m} of tournament {tournament_name}: lost with {score_t2 - score_t1} points.")

