floors = int(input())
rooms = int(input())
room_prefix = ""

for i in range(floors, 0, -1):
    if i == floors:
        room_prefix = "L"
    elif i % 2 == 0:
        room_prefix = "O"
    elif i % 2 == 1:
        room_prefix = "A"
    for f in range(0, rooms):
        print(f"{room_prefix}{i}{f}", end=" ")
    print()
