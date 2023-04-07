turns_loop = int(input())

score = 0
dice_0_9 = 0
dice_10_19 = 0
dice_20_29 = 0
dice_30_39 = 0
dice_40_50 = 0
dice_fail = 0

for i in range(0, turns_loop):
    new_turn_number = int(input())
    if 0 <= new_turn_number < 10:
        score += new_turn_number * 0.2
        dice_0_9 += 1
    elif 10 <= new_turn_number < 20:
        score += new_turn_number * 0.3
        dice_10_19 += 1
    elif 20 <= new_turn_number < 30:
        score += new_turn_number * 0.4
        dice_20_29 += 1
    elif 30 <= new_turn_number < 40:
        score += 50
        dice_30_39 += 1
    elif 40 <= new_turn_number <= 50:
        score += 100
        dice_40_50 += 1
    elif new_turn_number < 0 or new_turn_number > 50:
        score = score/2
        dice_fail += 1

print(f"{score:.2f}")
print(f"From 0 to 9: {(dice_0_9/turns_loop)*100:.2f}%")
print(f"From 10 to 19: {(dice_10_19/turns_loop)*100:.2f}%")
print(f"From 20 to 29: {(dice_20_29/turns_loop)*100:.2f}%")
print(f"From 30 to 39: {(dice_30_39/turns_loop)*100:.2f}%")
print(f"From 40 to 50: {(dice_40_50/turns_loop)*100:.2f}%")
print(f"Invalid numbers: {(dice_fail/turns_loop)*100:.2f}%")
