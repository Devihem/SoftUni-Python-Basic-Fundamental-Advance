import copy


def kate_position(maze_lst: list):  # Kate current location
    kate_state = True
    for row in range(len(maze_lst)):
        for column in range(len(maze_lst[row])):
            if maze_lst[row][column] == "k":
                if row == 0 or row == len(maze_lst) - 1:

                    if column == 0:
                        if len(maze_lst[row]) < 2:
                            kate_state = False
                        elif row == 0:
                            if maze_lst[row][column + 1] != " " and maze_lst[row + 1][column] != " ":
                                kate_state = False
                        elif row == len(maze_lst) - 1:
                            if maze_lst[row][column + 1] != " " and maze_lst[row - 1][column] != " ":
                                kate_state = False

                    elif column == len(maze_lst[row]) - 1:
                        if len(maze_lst[row]) < 2:
                            kate_state = False
                        elif row == 0:
                            if maze_lst[row][column - 1] != " " and maze_lst[row + 1][column] != " ":
                                kate_state = False
                        elif row == len(maze_lst) - 1:
                            if maze_lst[row][column - 1] != " " and maze_lst[row - 1][column] != " ":
                                kate_state = False

                    else:
                        if row == 0:
                            if maze_lst[row][column - 1] != " " and maze_lst[row][column + 1] != " " and \
                                    maze_lst[row + 1][column] != " ":
                                kate_state = False
                        elif row == len(maze_lst) - 1:
                            if maze_lst[row][column - 1] != " " and maze_lst[row][column + 1] != " " and \
                                    maze_lst[row - 1][column] != " ":
                                kate_state = False

                elif column == 0 or column == len(maze_lst[row]) - 1:
                    if row == 0 and len(maze_lst) > 1:
                        if maze_lst[row - 1][column] != " ":
                            kate_state = False
                    elif row == len(maze_lst) - 1:
                        if maze_lst[row + 1][column] != " ":
                            kate_state = False
                    else:
                        if maze_lst[row - 1][column] != " " and maze_lst[row + 1][column] != " ":
                            kate_state = False
                return row, column, kate_state
    else:
        row, column = "END", "END"
        return row, column, kate_state


def kate_move_direction(k_row: int, k_column: int, maze_lst: list, moves: int):  # Kate move/step on the maze

    # First looking for " " free space in the matrix, if there is no free space look for the next path symbol "-".
    path_symbol = " "
    replace_symbol = "-"
    step = 1

    while True:
        # Move UP
        if k_row != 0:
            if maze_lst[k_row - 1][k_column] == path_symbol:
                maze_lst[k_row - 1][k_column] = "k"
                maze_lst[k_row][k_column] = replace_symbol
                break

        # Move DOWN
        if k_row != len(maze_lst) - 1:
            if maze_lst[k_row + 1][k_column] == path_symbol:
                maze_lst[k_row + 1][k_column] = "k"
                maze_lst[k_row][k_column] = replace_symbol
                break

        # Move LEFT
        if k_column != 0:
            if maze_lst[k_row][k_column - 1] == path_symbol:
                maze_lst[k_row][k_column - 1] = "k"
                maze_lst[k_row][k_column] = replace_symbol
                break

        # Move RIGHT
        if k_column != len(maze_lst[k_row]) - 1:
            if maze_lst[k_row][k_column + 1] == path_symbol:
                maze_lst[k_row][k_column + 1] = "k"
                maze_lst[k_row][k_column] = replace_symbol
                break

        # final pathway  Step Back = "-" or END

        if path_symbol == "-":
            maze_lst = "END"
            return maze_lst, moves
        path_symbol = "-"
        replace_symbol = "+"
        step = -1  # Counting back the steps for proper calculation

    moves += step
    return maze_lst, moves


# Maze generation
maze_length = int(input())
original_maze = []
needed_moves = 0
max_moves = 0
one_way_out = False

for maze_row in range(maze_length):
    original_maze.append(list(input()))

# Copy of the maze  for re-rolls
maze_r_c = copy.deepcopy(original_maze)
# Maze loop
while True:

    # Kate position
    kate_row, kate_column, kate_looking_for_way_out = kate_position(maze_r_c)
    if kate_row == "END":
        break
    if not kate_looking_for_way_out:
        needed_moves += 1
        one_way_out = True
        original_maze[kate_row][kate_column] = "#"
        maze_r_c = copy.deepcopy(original_maze)
        if max_moves < needed_moves:
            max_moves = needed_moves
        needed_moves = 0
        continue

    # Kate move on maze
    maze_r_c, needed_moves = kate_move_direction(kate_row, kate_column, maze_r_c, needed_moves)

    # ( Un-comment Line 139 & 140 for Visual representation )
    [print(*row) for row in maze_r_c]
    print("-------------------------------")

    if maze_r_c == "END":
        break

if one_way_out:
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")

