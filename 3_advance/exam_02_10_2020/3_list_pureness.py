from collections import deque


def best_list_pureness(numbers_list: list, rotate_count):
    numbers_list = deque(numbers_list)
    highest_pureness = float('-inf')
    highest_pureness_count = float('-inf')

    for counter in range(rotate_count+1):
        current_pureness = 0
        for index in range(len(numbers_list)):
            current_pureness += numbers_list[index] * index

        if current_pureness > highest_pureness:
            highest_pureness = current_pureness
            highest_pureness_count = counter

        numbers_list.appendleft(numbers_list.pop())

    return f"Best pureness {highest_pureness} after {highest_pureness_count} rotations"


test = ([-1, 0, -1, -1], 1)
result = best_list_pureness(*test)
print(result)

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
