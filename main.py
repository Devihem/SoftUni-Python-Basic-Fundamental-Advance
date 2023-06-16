from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

healing_items = {
    30: 'Patch',
    40: 'Bandage',
    100: "MedKit"
}

healing_count = {
    'Patch': 0,
    'Bandage': 0,
    "MedKit": 0
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    healing_resource = textile + medicament

    if healing_resource in healing_items:
        healing_count[healing_items[healing_resource]] += 1

    elif healing_resource > 100:
        healing_count['MedKit'] += 1
        healing_resource -= 100
        medicaments[-1] += healing_resource

    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print('Textiles and medicaments are both empty.')
elif not textiles:
    print('Textiles are empty.')
elif not medicaments:
    print('Medicaments are empty.')

for item, value in sorted(healing_count.items(), key=lambda x: (x[1] * -1, x[0])):
    if value:
        print(f'{item} - {value}')

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in sorted(medicaments, reverse=True))}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in sorted(textiles, reverse=True))}")