def chess_x_y(matrix_row, matrix_col):
    chess_row = 8 - matrix_row
    chess_col = chr(97 + matrix_col)
    return f'{chess_col}{chess_row}'


board_size = 8
chess_board = [input().split() for _ in range(board_size)]

moves_pawns = [
    (-1, 0),  # White
    (1, 0)  # Black
]

w_r, w_c = 10, 10
b_r, b_c = 10, 10

for row in range(board_size):
    for col in range(board_size):

        if chess_board[row][col] == 'w':
            w_r, w_c = row, col

        elif chess_board[row][col] == 'b':
            b_r, b_c = row, col

while True:

    # White Attack
    for element in chess_board[w_r - 1]:
        if element == 'b':
            if chess_board[w_r - 1].index('b') == w_c + 1 or chess_board[w_r - 1].index('b') == w_c - 1:
                w_c = chess_board[w_r - 1].index('b')
                w_r = w_r - 1
                print(f"Game over! White win, capture on {chess_x_y(w_r, w_c)}.")
                quit()
    else:
        chess_board[w_r][w_c] = '-'
        w_r -= 1
        chess_board[w_r][w_c] = 'w'

    # Black attack
    for element in chess_board[b_r + 1]:
        if element == 'w':
            if chess_board[b_r + 1].index('w') == b_c + 1 or chess_board[b_r + 1].index('w') == b_c - 1:
                b_c = chess_board[b_r + 1].index('w')
                b_r = b_r + 1
                print(f"Game over! Black win, capture on {chess_x_y(b_r, b_c)}.")
                quit()
    else:
        chess_board[b_r][b_c] = '-'
        b_r += 1
        chess_board[b_r][b_c] = 'b'

    if w_r == 0:
        print(f"Game over! White pawn is promoted to a queen at {chess_x_y(w_r, w_c)}.")
        break

    elif b_r == 7:
        print(f"Game over! Black pawn is promoted to a queen at {chess_x_y(b_r, b_c)}.")
        break
