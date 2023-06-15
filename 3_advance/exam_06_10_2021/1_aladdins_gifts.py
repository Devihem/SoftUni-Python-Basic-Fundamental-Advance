from collections import deque

materials = deque([int(x) for x in input().split()])
magic_lvl = deque([int(x) for x in input().split()])

gifts_dict = {
    'Diamond Jewellery': 0,
    'Gemstone': 0,
    'Gold': 0,
    'Porcelain Sculpture': 0,
}

while materials and magic_lvl:

    current_material = materials.pop()
    current_magic = magic_lvl.popleft()
    current_sum = current_magic + current_material

    if current_sum < 100:
        if current_sum % 2 == 0:
            current_sum = current_material * 2 + current_magic * 3
        else:
            current_sum *= 2
    elif current_sum > 499:  # 450
        current_sum /= 2

    if 100 <= current_sum < 200:
        gifts_dict['Gemstone'] += 1
    elif 200 <= current_sum < 300:
        gifts_dict['Porcelain Sculpture'] += 1
    elif 300 <= current_sum < 400:
        gifts_dict['Gold'] += 1
    elif 400 <= current_sum < 500:
        gifts_dict['Diamond Jewellery'] += 1

gift_count_list = list(gifts_dict.values())
if (gift_count_list[0] > 0 and gift_count_list[2] > 0) or \
        (gift_count_list[3] > 0 and gift_count_list[1] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print("Materials left: ", end='')
    print(*materials, sep=', ')

if magic_lvl:
    print("Magic left: ", end='')
    print(*magic_lvl, sep=', ')

for item, value in gifts_dict.items():
    if value > 0:
        print(f"{item}: {value}")
