from collections import deque

material_boxes = deque([int(x) for x in input().split()])
magic_values = deque([int(x) for x in input().split()])

presents = {400: ['Bicycle', 0], 300: ['Teddy bear', 0], 250: ['Wooden train', 0], 150: ['Doll', 0]}

while material_boxes and magic_values:
    material = material_boxes.pop()
    magic = magic_values.popleft()
    magic_level = material * magic

    if magic_level in presents.keys():
        presents[magic_level][1] += 1
        continue

    if magic_level < 0:
        material_boxes.append(material + magic)

    elif magic_level > 0:
        material_boxes.append(material + 15)

    elif magic == 0 or material == 0:
        if magic == 0 and material == 0:
            continue
        elif magic == 0:
            material_boxes.append(material)
        elif material == 0:
            magic_values.appendleft(magic)

if (presents[150][1] > 0 and presents[250][1] > 0) or (presents[300][1] > 0 and presents[400][1] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_boxes:
    print("Materials left: ", end=''), print(*list(reversed(material_boxes)), sep=', ')

if magic_values:
    print("Magic left: ", end=''), print(*magic_values, sep=', ')

[print(f"{data[1][0]}: {data[1][1]}") for data in (sorted(presents.items(), key=lambda k: k[1])) if data[1][1] > 0]
