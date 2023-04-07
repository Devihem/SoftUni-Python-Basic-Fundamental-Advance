import random
print("Welcome , the game is Rock Scissors Paper with 5 rounds")
rock = "Rock"
scissors = "Scissors"
paper = "Paper"
ai_points = 0
player_points = 0

for game in range(5):
    player_move = input("Enter your move : [R]ock ,[S]cissors or [P]aper : ")
    if player_move not in "RSP":
        print("Use only [ R , S , P] moves, the round is. The round is invalid!")
        continue
    if player_move == "R":
        player_move = rock
    elif player_move == "S":
        player_move = scissors
    elif player_move == "P":
        player_move = paper

    ai_move = random.randint(1, 3)
    if ai_move == 1:
        ai_move = rock
    elif ai_move == 2:
        ai_move = scissors
    elif ai_move == 3:
        ai_move = paper

    print(f"\nPlayer [{player_move}] --VS-- AI [{ai_move}]\n")

    if player_move == ai_move:
        player_points += 1
        ai_points += 1
        print(f"Round[{game+1}] - Result: DRAW !\n")
    elif player_move == rock:
        if ai_move == scissors:
            player_points += 1
            print(f"Round[{game+1}] - Result: Player Win !\n")
        else:
            ai_points += 1
            print(f"Round[{game+1}] - Result: AI Win!\n")
    elif player_move == scissors:
        if ai_move == paper:
            player_points += 1
            print(f"Round[{game+1}] - Result: Player Win !\n")
        else:
            ai_points += 1
            print(f"Round[{game+1}] - Result: AI Win!\n")
    elif player_move == paper:
        if ai_move == rock:
            player_points += 1
            print(f"Round[{game+1}] - Result: Player Win !\n")
        else:
            ai_points += 1
            print(f"Round[{game+1}] - Result: AI Win!\n")


print(f"Player [{player_points}] VS AI [{ai_points}]")
