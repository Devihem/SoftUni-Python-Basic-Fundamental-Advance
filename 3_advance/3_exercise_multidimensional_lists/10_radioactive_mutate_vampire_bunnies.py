from copy import deepcopy


def player_position(map_maze: list, max_row: int, max_col: int):
    for map_row in range(max_row):
        for map_col in range(max_col):
            if map_maze[map_row][map_col] == 'P':
                return map_row, map_col


def player_movement_func(map_maze: list, move_command: str, player_row: int, player_col: int, max_row: int,
                         max_col: int):
    dead_flag = False
    if move_command == 'U' and player_row > 0:
        map_maze[player_row][player_col] = '.'
        if map_maze[player_row - 1][player_col] == 'B':
            dead_flag = True
        map_maze[player_row - 1][player_col] = 'P'

    elif move_command == 'D' and player_row < max_row - 1:
        map_maze[player_row][player_col] = '.'
        if map_maze[player_row + 1][player_col] == '.':
            dead_flag = True
        map_maze[player_row + 1][player_col] = 'P'

    elif move_command == 'L' and player_col > 0:
        map_maze[player_row][player_col] = '.'
        if map_maze[player_row][player_col - 1] == '.P':
            dead_flag = True
        map_maze[player_row][player_col - 1] = 'P'

    elif move_command == 'R' and player_col < max_col - 1:
        map_maze[player_row][player_col] = '.'
        if map_maze[player_row + 1][player_col] == '.':
            dead_flag = True
        map_maze[player_row + 1][player_col] = 'P'

    return map_maze, dead_flag


def bunny_mutation(map_maze: list):
    mutated_maze = deepcopy(map_maze)

    for row in range(len(map_maze)):
        for column in range(len(map_maze[row])):
            if map_maze[row][column] == 'B':
                if row > 0:
                    mutated_maze[row - 1][column] = 'B'
                if row < len(map_maze) - 1:
                    mutated_maze[row + 1][column] = 'B'
                if column > 0:
                    mutated_maze[row][column - 1] = 'B'
                if column < len(map_maze[row]) - 1:
                    mutated_maze[row][column + 1] = 'B'
    return mutated_maze


def player_dead_check(map_maze: list):
    for map_dead_row in map_maze:
        for el_col in map_dead_row:
            if el_col == 'P':
                return False
    return True


maze_row, maze_col = map(int, input().split())
maze = [[x for x in list(input())] for _ in range(maze_row)]

player_movement = list(input())
player_escaped_flag = False
player_dead_flag = False
special_dead_flag = False

new_p_row = 0
new_p_col = 0

for move in player_movement:
    # Player Position
    p_row, p_col = player_position(maze, maze_row, maze_col)

    # Player Move , If player hit a bunny special Flag is triggered
    maze, special_dead_flag = player_movement_func(maze, move, p_row, p_col, maze_row, maze_col)

    # Player New position
    new_p_row, new_p_col = player_position(maze, maze_row, maze_col)

    if special_dead_flag:
        maze[new_p_row][new_p_col] = 'B'

    # If the player position didn't change after MOVE => Player escaped
    if new_p_row == p_row and new_p_col == p_col:
        player_escaped_flag = True

    # Mutate the bunnies  using deepcopy of the maze
    maze = bunny_mutation(maze)

    # If there is no player on map => player Dead
    player_dead_flag = player_dead_check(maze)

    if player_escaped_flag:
        break
    if player_dead_flag:
        break
    if special_dead_flag:
        break

# Print Win or Lose  ( Win Must be first in if statement )

if player_escaped_flag and special_dead_flag == False:
    # Correction to clear the last player position
    if maze[new_p_row][new_p_col] == 'P':
        maze[new_p_row][new_p_col] = '.'
    [print(''.join(row)) for row in maze]
    print(f"won: {new_p_row} {new_p_col}")

elif player_dead_flag:
    [print(''.join(row)) for row in maze]
    print(f"dead: {new_p_row} {new_p_col}")
