number_of_presents = int(input())
matrix_size = int(input())
matrix = []
s_loc_r = 0
s_loc_c = 0
total_good_kids = 0
current_good_kid = 0
delivered_presents = 0

# Possible directions
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

# Creating the grid , finding santa - S location , Count the good kids - V
for row_count in range(matrix_size):
    new_row = input().split()
    matrix.append(new_row)
    if 'S' in new_row:
        s_loc_r, s_loc_c = (row_count, new_row.index('S'))
    if 'V' in new_row:
        total_good_kids += new_row.count('V')

# Loop break if no more presents or no more good kids and  on command 'Christmas morning'
while True:
    # Command input
    move = input()

    # Command 'Christmas morning' - Stop the loop
    if move == 'Christmas morning':
        break

    new_r, new_c = directions[move]
    r, c = new_r + s_loc_r, new_c + s_loc_c

    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        # Normal move - if good kid - give present
        if matrix[r][c] == 'V':
            delivered_presents += 1
            number_of_presents -= 1
            current_good_kid += 1

        # Cookie event trigger  up,down,left,right  receive a gift if there is a house
        elif matrix[r][c] == 'C':
            for key in directions.keys():
                cookie_r, cookie_c = r + directions[key][0], c + directions[key][1]
                if matrix[cookie_r][cookie_c] in ['V', 'X']:
                    if matrix[cookie_r][cookie_c] == 'V':
                        current_good_kid += 1

                    matrix[cookie_r][cookie_c] = '-'
                    delivered_presents += 1
                    number_of_presents -= 1

        # if the kid is naughty don't give present
        matrix[s_loc_r][s_loc_c] = '-'
        matrix[r][c] = 'S'
        s_loc_r, s_loc_c = r, c

    # If all good kids have present - Stop the loop
    if current_good_kid >= total_good_kids:
        break

    # If no more presents - Stop the loop
    # The check for no presents is after the check for good kids
    if number_of_presents <= 0:
        print(f"Santa ran out of presents!")
        break

# print the matrix
[print(*row) for row in matrix]

# end print on condition
if current_good_kid >= total_good_kids:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_good_kids - current_good_kid} nice kid/s.")
