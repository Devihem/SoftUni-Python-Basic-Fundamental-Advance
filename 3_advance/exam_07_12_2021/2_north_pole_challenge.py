rows, columns = map(int, input().split(', '))
santa_map = []
santa_r = 0
santa_c = 0
items_count = 0
items_dict = {
    "D": 0,  # Decoration
    "G": 0,  # Gifts
    "C": 0,  # Cookies
}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    santa_map_row = input().split()
    for el in santa_map_row:
        if el == 'Y':
            santa_r = row
            santa_c = santa_map_row.index('Y')
        elif el != '.':
            items_count += 1

    santa_map.append(santa_map_row)

while items_count > 0:

    command = input()
    if command == 'End':
        break

    dir_name, steps = command.split('-')

    for step_count in range(int(steps)):
        dir_r, dir_c = directions[dir_name]

        # Moving out - Place x
        santa_map[santa_r][santa_c] = 'x'

        # resize - R
        santa_r = santa_r + dir_r
        if santa_r < 0:
            santa_r = rows - 1
        elif santa_r > rows - 1:
            santa_r = 0

        # resize - C
        santa_c = santa_c + dir_c
        if santa_c < 0:
            santa_c = columns - 1
        elif santa_c > columns - 1:
            santa_c = 0

        if santa_map[santa_r][santa_c] not in ['.', 'x']:
            items_dict[santa_map[santa_r][santa_c]] += 1
            items_count -= 1
        santa_map[santa_r][santa_c] = 'Y'

        if items_count <= 0:
            break
else:
    print("Merry Christmas!")

print(f"You've collected:"
      f"\n- {items_dict['D']} Christmas decorations"
      f"\n- {items_dict['G']} Gifts"
      f"\n- {items_dict['C']} Cookies")

[print(' '.join(x)) for x in santa_map]
