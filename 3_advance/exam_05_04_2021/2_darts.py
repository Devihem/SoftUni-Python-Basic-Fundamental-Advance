player_1, player_2 = input().split(', ')

score_dict = {
    player_1: [501, 0],
    player_2: [501, 0],
}

board = [input().split() for _ in range(7)]

while True:
    for player_turn in score_dict.keys():
        shot_r, shot_c = [int(x) for x in input().strip('(').strip(')').split(', ')]

        score_dict[player_turn][1] += 1

        if 0 <= shot_r < 7 and 0 < shot_c < 7:

            multiplayer_sum = int(board[shot_r][0]) + int(board[shot_r][6]) + int(board[0][shot_c]) + int(
                board[6][shot_c])

            if board[shot_r][shot_c] == 'B':
                score_dict[player_turn][0] -= 501

            elif board[shot_r][shot_c] == 'D':
                score_dict[player_turn][0] -= multiplayer_sum * 2

            elif board[shot_r][shot_c] == 'T':
                score_dict[player_turn][0] -= multiplayer_sum * 3

            else:
                score_dict[player_turn][0] -= int(board[shot_r][shot_c])

        if score_dict[player_turn][0] <= 0:
            print(f"{player_turn} won the game with {score_dict[player_turn][1]} throws!")
            quit()
