from collections import deque


def road_crossing(green_timer: int, free_timer: int, car_order: deque, car_count: int):
    current_car = deque([])
    last_car_name = ""
    for second in range(green_timer):
        if len(current_car) == 0 and len(car_order) > 0:
            car_count += 1
            last_car_name = car_order.popleft()
            current_car = deque([letter for letter in last_car_name])
        if len(current_car) > 0:
            current_car.popleft()

    for second in range(free_timer):
        if len(current_car) > 0:
            current_car.popleft()

    if current_car:
        print("A crash happened!")
        print(f"{last_car_name} was hit at {current_car[0]}.")
        quit()

    return car_order, car_count


green_light_time = int(input())
free_pass_time = int(input())
car_queue = deque([])
total_car_count = 0

while True:

    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{total_car_count} total cars passed the crossroads.")
        break

    elif command == "green":
        car_queue , total_car_count = road_crossing(green_light_time, free_pass_time, car_queue, total_car_count)

    else:
        car_queue.append(command)
