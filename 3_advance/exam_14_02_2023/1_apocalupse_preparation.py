from collections import deque

textiles = deque([int(x) for x in input().split(' ')])
medicaments = deque([int(x) for x in input().split(' ')])

items_table = {
    30: ['Patch', 0],
    40: ['Bandage', 0],
    100: ['MedKit', 0]
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medic = medicaments.pop()
    current_sum = current_medic + current_textile

    if current_sum in items_table.keys():
        items_table[current_sum][1] += 1
        continue
    elif current_sum > 100:
        items_table[100][1] += 1
        leftover_points = current_sum - 100
        upgraded_medic = medicaments.pop() + leftover_points
        medicaments.append(upgraded_medic)
        continue
    else:
        current_medic += 10
        medicaments.append(current_medic)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

ordered_list = sorted(items_table.items(), key=lambda k: (-k[1][1], k[1][0]))
[print(f'{x[1][0]} - {x[1][1]}') for x in ordered_list if x[1][1] > 0]


if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in reversed(medicaments)])}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
