# sloppy solved
def find_second_b_lock():
    for row_b in range(maze_size):
        for col_b in range(maze_size):
            if maze[row_b][col_b] == 'B':
                return row_b, col_b


maze = []
food = 0
snake_r, snake_c = 0, 0
maze_size = int(input())
for row in range(maze_size):
    new_line = list(input())
    if 'S' in new_line:
        snake_r, snake_c = row, new_line.index('S')
        new_line[snake_c] = '.'
    maze.append(new_line)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while food < 10:
    dir_r, dir_c = directions[input()]

    check_r = dir_r + snake_r
    check_c = dir_c + snake_c
    if 0 > check_r or check_r >= maze_size or 0 > check_c or check_c >= maze_size:
        print("Game over!")
        break

    snake_r = snake_r + dir_r
    snake_c = snake_c + dir_c

    if maze[snake_r][snake_c] == '*':
        food += 1
        maze[snake_r][snake_c] = '.'

    elif maze[snake_r][snake_c] == "B":
        maze[snake_r][snake_c] = '.'
        snake_r, snake_c = find_second_b_lock()
        maze[snake_r][snake_c] = '.'
    else:
        maze[snake_r][snake_c] = '.'

else:
    maze[snake_r][snake_c] = 'S'
    print("You won! You fed the snake.")

print(f"Food eaten: {food}")
[print(''.join(row_print)) for row_print in maze]
