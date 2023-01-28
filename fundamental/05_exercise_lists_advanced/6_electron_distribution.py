electrons = int(input())
list_with_shells = ["0"]
current_shell_index = 0
while electrons > 0:
    if int(list_with_shells[current_shell_index]) == 2 * current_shell_index ** 2:
        list_with_shells.append("0")
        current_shell_index += 1
    list_with_shells[-1] = str(int(list_with_shells[-1]) + 1)
    electrons -= 1

list_with_shells = [int(number) for number in list_with_shells if number != "0"]
print(list_with_shells)
