command_string = list(input())
final_result = []

index = -1
explosion = 0
for item in command_string:
    index += 1
    if item == ">":
        print(command_string[index + 1])
        explosion = int(command_string[index + 1])

    if explosion > 0:
        explosion -= 1
        continue

    final_result.append(item)

print(command_string)
print(final_result)
