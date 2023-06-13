from collections import deque


def check_bombs_count():
    full_pouch_flag = all([True if bomb_info[1] >= 3 else False for bomb_info in bombs_dict.values()])
    return full_pouch_flag


bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = deque([int(x) for x in input().split(', ')])

bombs_dict = {
    60: ['Cherry Bombs', 0],
    40: ['Datura Bombs', 0],
    120: ['Smoke Decoy Bombs', 0],
}

while bomb_effects and bomb_casings:

    bomb_effect = bomb_effects.popleft()
    bomb_case = bomb_casings.pop()

    if bomb_effect + bomb_case in bombs_dict.keys():
        bombs_dict[bomb_effect + bomb_case][1] += 1
    else:
        bomb_effects.appendleft(bomb_effect)
        bomb_casings.append(bomb_case - 5)

    if check_bombs_count():
        break

if check_bombs_count():
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(b_ef) for b_ef in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(b_cs) for b_cs in bomb_casings])}")
else:
    print("Bomb Casings: empty")

[print(f'{bomb_name}: {count}') for bomb_name, count in bombs_dict.values()]
