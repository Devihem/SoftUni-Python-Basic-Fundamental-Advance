number_of_lines = int(input())
max_length = 0
max_length_set = {}
for _ in range(number_of_lines):
    set_first = set()
    set_second = set()

    start_first, first_second, end_second = input().split(",")
    end_first, start_second = first_second.split("-")

    for number_first_set in range(int(start_first), int(end_first)+1):
        set_first.add(number_first_set)

    for number_second_set in range(int(start_second), int(end_second)+1):
        set_second.add(number_second_set)

    if len(set_first.intersection(set_second)) > max_length:
        max_length = len(set_first.intersection(set_second))
        max_length_set = set_first.intersection(set_second)

print(f"Longest intersection is [", end='')
print(*max_length_set, sep=', ', end='')
print(f"] with length {max_length}")
