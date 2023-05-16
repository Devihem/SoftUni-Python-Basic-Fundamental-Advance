# main_data
matrix = []
position_r, position_c = (0, 0)
all_targets = 0
hit_targets = 0
hit_targets_locations = []

# Possible directions
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

# Creating the matrix , Finding A-Location row, col , Count the 'x' targets in the matrix.
for row in range(5):
    new_row = input().split()
    matrix.append(new_row)
    if 'A' in new_row:
        position_r, position_c = (row, new_row.index('A'))
    if 'x' in new_row:
        all_targets += new_row.count('x')

# Loop for given index for exact count of commands
for _ in range(int(input())):

    # Split the input for both commands Move and Shoot
    command, direction, *steps = input().split()

    # Giving direction for both commands
    r, c = directions[direction]

    # Command Move - move only on locations with '.' in the matrix for N steps.
    if command == 'move':
        for _ in range(int(steps[0])):
            new_r, new_c = position_r + r, position_c + c
            if 0 <= new_r < 5 and 0 <= new_c < 5:
                if matrix[new_r][new_c] == '.':
                    matrix[position_r][position_c] = '.'
                    matrix[new_r][new_c] = 'A'
                    position_r, position_c = new_r, new_c

    # Command Shoot. Bullet travel all across the grid until vanish or hit a target
    elif command == 'shoot':
        bullet_r, bullet_c = position_r, position_c
        for _ in range(5):
            new_bullet_r, new_bullet_c = bullet_r + r, bullet_c + c
            if 0 <= new_bullet_r < 5 and 0 <= new_bullet_c < 5:
                if matrix[new_bullet_r][new_bullet_c] == 'x':
                    matrix[new_bullet_r][new_bullet_c] = '.'
                    hit_targets_locations.append([new_bullet_r, new_bullet_c])
                    hit_targets += 1
                    break
            bullet_r, bullet_c = new_bullet_r, new_bullet_c

    # If all targets hit end the shooting
    if hit_targets == all_targets:
        print(f"Training completed! All {all_targets} targets hit.")
        break

else:
    # If the loop / shooting end and three are more targets print 'Fail-statement'
    print(f"Training not completed! {all_targets - hit_targets} targets left.")

print(*hit_targets_locations, sep='\n')
