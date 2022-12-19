first_row = int(input())
second_row = int(input())
magic_number = int(input())
counter = 0
place = False

for x1 in range(first_row, second_row+1):
    if place != False:
        break
    for x2 in range(first_row, second_row+1):
        counter += 1
        if x1 + x2 == magic_number:
            place = counter
            print(f"Combination N:{place} ({x1} + {x2} = {magic_number})")

if place == False:
    print(f"{counter} combinations - neither equals {magic_number}")
