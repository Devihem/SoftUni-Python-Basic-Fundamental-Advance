
car_set = set()
for _ in range(int(input())):
    command, car = input().split(', ')
    if command == "IN":
        car_set.add(car)
    elif command == "OUT" and car_set:
        car_set.remove(car)
if car_set:
    print(*car_set, sep='\n')
else:
    print("Parking Lot is Empty")