# sloppy solved

maze_size = int(input())
maze = [input().split() for _ in range(maze_size)]

path = []
player_r, player_c = 0, 0
collected_coins = 0

for row in range(maze_size):
    for col in range(maze_size):
        if maze[row][col] == 'P':
            maze[row][col] = '0'
            player_r, player_c = row, col
            path.append([player_r, player_c])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while collected_coins < 100:
    new_r, new_c = directions[input()]

    new_player_r = new_r + player_r
    if new_player_r < 0:
        new_player_r = maze_size - 1
    elif new_player_r > maze_size - 1:
        new_player_r = 0

    new_player_c = new_c + player_c
    if new_player_c < 0:
        new_player_c = maze_size - 1
    elif new_player_c > maze_size - 1:
        new_player_c = 0

    if maze[new_player_r][new_player_c] == 'X':
        collected_coins = collected_coins // 2
        print(f"Game over! You've collected {collected_coins} coins.")
        path.append([new_player_r, new_player_c])
        break

    collected_coins += int(maze[new_player_r][new_player_c])
    maze[new_player_r][new_player_c] = '0'

    path.append([new_player_r, new_player_c])

    player_r = new_player_r
    player_c = new_player_c

else:
    print(f"You won! You've collected {collected_coins} coins.")
print('Your path:')
[print(r_c) for r_c in path]
