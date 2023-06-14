from collections import deque

fireworks_effects = deque([int(x) for x in input().split(', ')])

explosive_power = deque([int(x) for x in input().split(', ')])

fireworks_dict = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,

}

while fireworks_effects and explosive_power:
    current_effects = fireworks_effects.popleft()
    current_power = explosive_power.pop()

    if current_effects <= 0 and current_power <= 0:
        continue
    elif current_effects <= 0:
        explosive_power.append(current_power)
        continue
    elif current_power <= 0:
        fireworks_effects.appendleft(current_effects)
        continue

    current_sum = current_power + current_effects

    if current_sum % 3 == 0 or current_sum % 5 == 0:
        if current_sum % 3 == 0 and current_sum % 5 == 0:
            fireworks_dict['Crossette Fireworks'] += 1
        elif current_sum % 3 != 0 and current_sum % 5 == 0:
            fireworks_dict['Willow Fireworks'] += 1
        else:
            fireworks_dict['Palm Fireworks'] += 1

        if all([True if firework >= 3 else False for firework in fireworks_dict.values()]):
            print("Congrats! You made the perfect firework show!")
            break

        continue

    current_effects = current_effects - 1
    fireworks_effects.append(current_effects)
    explosive_power.append(current_power)
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print("Firework Effects left:", end=' ')
    print(*fireworks_effects, sep=', ')

if explosive_power:
    print("Explosive Power left:", end=' ')
    print(*explosive_power, sep=', ')

[print(f'{name}: {value}') for name, value in fireworks_dict.items()]
