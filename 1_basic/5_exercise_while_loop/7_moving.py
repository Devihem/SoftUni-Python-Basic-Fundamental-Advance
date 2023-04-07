room_size_1 = int(input())
room_size_2 = int(input())
room_size_3 = int(input())

left_space = room_size_1 * room_size_2 * room_size_3

while left_space > 0:
    used_space = input()
    if used_space == "Done":
        print(f"{left_space} Cubic meters left.")
        break
    else:
        used_space = int(used_space)
        left_space = left_space - used_space
else:
    print(f"No more free space! You need {-left_space} Cubic meters more.")
