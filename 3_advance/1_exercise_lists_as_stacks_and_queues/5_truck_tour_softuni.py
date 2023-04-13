from collections import deque

gas_stations_list = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
smallest_index = "None"
current_index = -1
tour_complete = False

while not tour_complete:
    current_index += 1
    starting_fuel = 0

    first_stop = gas_stations_list.popleft()
    gas_stations_list.appendleft(first_stop)
    gas_stations_list.append(first_stop)

    for gas_station in gas_stations_list:
        fuel, next_stop = gas_station
        starting_fuel += fuel
        if starting_fuel < next_stop:
            break
        starting_fuel -= next_stop
    else:
        smallest_index = current_index
        tour_complete = True

    gas_stations_list.popleft()

print(smallest_index)
