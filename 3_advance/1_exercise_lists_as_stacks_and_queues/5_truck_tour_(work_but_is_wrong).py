number_of_stops = int(input())
amount_of_fuel = 0
smallest_index = 0

for stop in range(number_of_stops):

    petrol_pump_info = input().split()

    fuel = int(petrol_pump_info[0])
    next_distance = int(petrol_pump_info[1])

    if fuel + amount_of_fuel < next_distance:
        amount_of_fuel = 0
        smallest_index = int(stop) + 1
        continue

    amount_of_fuel += fuel
    amount_of_fuel -= next_distance

print(smallest_index)
