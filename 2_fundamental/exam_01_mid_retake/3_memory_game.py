game_board = input().split()
moves = 0
flag = False
while True:
    command = input()
    if command == "end":
        if flag:
            break
        else:
            print(f"Sorry you lose :(\n{' '.join(game_board)}")
        break
    if flag:
        continue

    guess_1, guess_2 = command.split()
    guess_1 = int(guess_1)
    guess_2 = int(guess_2)
    moves += 1
    if guess_1 == guess_2 or guess_1 not in range(len(game_board)) or guess_2 not in range(len(game_board)):
        game_board.insert(len(game_board) // 2, f"-{moves}a")
        game_board.insert(len(game_board) // 2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif game_board[guess_1] == game_board[guess_2]:
        current_element = game_board[guess_1]
        if guess_2 > guess_1:
            game_board.pop(guess_2)
            game_board.pop(guess_1)
        else:
            game_board.pop(guess_1)
            game_board.pop(guess_2)
        print(f"Congrats! You have found matching elements - {current_element}!")
    else:
        print("Try again!")

    if len(game_board) == 0:
        print(f"You have won in {moves} turns!")
        flag = True
