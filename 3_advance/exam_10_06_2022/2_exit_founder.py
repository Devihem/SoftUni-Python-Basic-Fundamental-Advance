from collections import deque

matrix_size = 6
players = deque(input().split(', '))
matrix = [input().split() for x in range(matrix_size)]
wall_penalty = []

while True:
    new_r, new_c = [int(x) for x in input().strip('(').strip(')').split(', ')]

    current_player = players.popleft()
    if current_player in wall_penalty:
        wall_penalty.remove(current_player)
        players.append(current_player)
        continue

    if matrix[new_r][new_c] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif matrix[new_r][new_c] == 'T':
        print(f"{current_player} is out of the game! The winner is {players[0]}.")
        break

    elif matrix[new_r][new_c] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        wall_penalty.append(current_player)

    players.append(current_player)
