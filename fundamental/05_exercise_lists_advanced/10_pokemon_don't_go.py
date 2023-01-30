distance = [int(number) for number in input().split()]
removed_number_total = 0
while len(distance) != 0:
    index = len(distance) - 1
    command = int(input())
    if command < 0:
        removed_number = distance.pop(0)
        distance.insert(0, distance[-1])
    elif command > index:
        removed_number = distance.pop(-1)
        distance.insert(index+1, distance[0])
    else:
        removed_number = distance.pop(command)
    for index_place, value in enumerate(distance):
        if value <= removed_number:
            distance[index_place] += removed_number
        else:
            distance[index_place] -= removed_number
    removed_number_total += removed_number

print(removed_number_total)