rooms = int(input())
free_chairs = 0
flag = True
for room in range(1, rooms+1):
    chairs_guests_information = input().split()
    chairs = len(chairs_guests_information[0])
    guests = int(chairs_guests_information[1])
    if chairs < guests:
        print(f"{guests - chairs} more chairs needed in room {room}")
        flag = False
    else:
        free_chairs += chairs - guests


else:
    if flag:
        print(f"Game On, {free_chairs} free chairs left")
