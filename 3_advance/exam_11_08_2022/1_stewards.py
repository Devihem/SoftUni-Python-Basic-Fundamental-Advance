from collections import deque

seats = deque([x for x in input().split(', ')])
numbers_1 = deque([int(x) for x in input().split(', ')])
numbers_2 = deque([int(x) for x in input().split(', ')])
counter = 0
seats_placed = []

while counter < 10 and len(seats_placed) < 3:

    current_number_1 = numbers_1.popleft()
    current_number_2 = numbers_2.pop()
    current_sum = current_number_1 + current_number_2

    generated_seat_1 = str(current_number_1) + f'{chr(current_sum)}'
    generated_seat_2 = str(current_number_2) + f'{chr(current_sum)}'

    counter += 1

    if generated_seat_1 in seats:
        seats_placed.append(generated_seat_1)
        seats.remove(generated_seat_1)
    elif generated_seat_2 in seats:
        seats_placed.append(generated_seat_2)
        seats.remove(generated_seat_2)
    else:
        numbers_1.append(current_number_1)
        numbers_2.appendleft(current_number_2)


print(f"Seat matches: {', '.join([str(x) for x in seats_placed])}")
print(f"Rotations count: {counter}")
