def flights(*args):
    destinations_dict = {}
    counter_index = -2
    for destination in (args[::2]):
        counter_index += 2
        if destination == 'Finish':
            return destinations_dict
        if destination not in destinations_dict.keys():
            destinations_dict[destination] = 0
        destinations_dict[destination] += args[counter_index + 1]


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
