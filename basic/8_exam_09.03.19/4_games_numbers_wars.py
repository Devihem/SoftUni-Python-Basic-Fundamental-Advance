player1_name = input()
player2_name = input()
score_p1 = 0
score_p2 = 0
while True:
    command = input()

    if command == "End of game":
        print(f"{player1_name} has {score_p1} points")
        print(f"{player2_name} has {score_p2} points")
        break
    else:
        card_p1 = int(command)

    card_p2 = int(input())

    if card_p1 > card_p2:
        score_p1 += (card_p1 - card_p2)
    elif card_p2 > card_p1:
        score_p2 += (card_p2 - card_p1)
    else:
        card_p1 = int(input())
        card_p2 = int(input())
        if card_p1 > card_p2:
            print("Number wars!")
            print(f"{player1_name} is winner with {score_p1} points")
            break
        elif card_p2 > card_p1:
            print("Number wars!")
            print(f"{player2_name} is winner with {score_p2} points")
            break
