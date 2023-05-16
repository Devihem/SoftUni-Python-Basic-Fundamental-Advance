directions = {
    'up': (-1, 0),
    'down': (0, -1),
    'left': (1, 0),
    'right': (0, 1),
}


move_list = ['up', 'up']
for key in move_list:
    r, c = directions[key]
    print(r,c)