energy = int(input())
won_battles = 0
while True:

    system_input = input()
    if system_input == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {energy}")
        break
    else:
        distance = int(system_input)

    if energy - distance < 0:
        energy_flag = True
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    else:
        energy -= distance
        won_battles += 1

    if won_battles % 3 == 0:
        energy += won_battles
