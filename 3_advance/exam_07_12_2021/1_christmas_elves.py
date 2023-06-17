from collections import deque

elfs = deque([int(x) for x in input().split()])
boxs = deque([int(x) for x in input().split()])

energy_used = 0
toys = 0
box_counter = 0

while elfs and boxs:

    current_elf = elfs.popleft()
    if current_elf < 5:
        continue

    current_box = boxs.pop()

    box_counter += 1

    if box_counter % 3 == 0:
        current_box *= 2

    if current_elf >= current_box:

        if box_counter % 5 == 0:
            toys += 0
        elif box_counter % 3 == 0:
            toys += 2
        else:
            toys += 1

        energy_used += current_box
        if box_counter % 5 == 0:
            current_elf -= current_box
        else:
            current_elf = (current_elf - current_box) + 1
        elfs.append(current_elf)

    else:
        elfs.append(current_elf * 2)
        if box_counter % 3 == 0:
            boxs.append(current_box // 2)
        else:
            boxs.append(current_box)

print(f"Toys: {toys}")
print(f"Energy: {energy_used}")

if elfs:
    print("Elves left: ", end='')
    print(*elfs, sep=', ')
if boxs:
    print("Boxes left: ", end='')
    print(*boxs, sep=', ')
