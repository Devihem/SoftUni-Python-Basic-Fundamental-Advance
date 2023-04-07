command_string = list(input())
final_result = []

index = -1
explosion = 0
for item in command_string:
    index += 1
    if item == ">":
        explosion += int(command_string[index + 1])

    if explosion > 0 and item != ">":
        explosion -= 1
        continue

    final_result.append(item)
print(''.join(final_result))
