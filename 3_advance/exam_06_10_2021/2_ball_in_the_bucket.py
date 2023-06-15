matrix_size = 6
total_score = 0
board = [input().split() for _ in range(matrix_size)]

for _ in range(3):
    new_r, new_c = [int(x) for x in input().strip('(').strip(')').split(', ')]
    if 0 <= new_r < matrix_size and 0 <= new_c < matrix_size:
        if board[new_r][new_c] == 'B':
            board[new_r][new_c] = '0'
            for row in board:
                total_score += int(row[new_c])

if total_score < 100:
    print(f"Sorry! You need {100 - total_score} points more to win a prize.")
else:
    prize = ''
    if total_score >= 300:
        prize = 'Lego Construction Set'
    elif total_score > 200:
        prize = 'Teddy Bear'
    else:
        prize = 'Football'

    print(f"Good job! You scored {total_score} points, and you've won {prize}.")