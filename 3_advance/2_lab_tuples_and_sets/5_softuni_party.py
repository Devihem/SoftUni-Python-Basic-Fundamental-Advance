reservation_set_standart = set()
reservation_set_vip = set()

for _ in range(int(input())):
    reservation = input()
    if reservation[0:1].isdigit():
        reservation_set_vip.add(reservation)
    else:
        reservation_set_standart.add(reservation)

while True:
    command = input()

    if command == "END":
        break

    if command[0:1].isdigit():
        reservation_set_vip.remove(command)
    else:
        reservation_set_standart.remove(command)
print(len(reservation_set_vip) + len(reservation_set_standart))
if reservation_set_vip:
    print(*(sorted(reservation_set_vip)), sep='\n')
if reservation_set_standart:
    print(*(sorted(reservation_set_standart)), sep='\n')
