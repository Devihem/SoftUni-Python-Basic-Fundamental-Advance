target_high = int(input())
changing_point = target_high - 30
jump_counter = 0
current_jump = 0
total_jump_counter = 0

while True:
    if current_jump > target_high and changing_point == target_high:
        print(f"Tihomir succeeded, he jumped over {target_high}cm after {total_jump_counter} jumps.")
        break
    if current_jump > changing_point:
        changing_point += 5
        jump_counter = 0
    elif jump_counter == 3:
        print(f"Tihomir failed at {changing_point}cm after {total_jump_counter} jumps.")
        break

    current_jump = int(input())
    jump_counter += 1
    total_jump_counter += 1
