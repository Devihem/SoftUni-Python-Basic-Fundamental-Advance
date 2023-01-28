wagon_numbers = [0 for x in range(0, int(input()))]

while True:
    command = input().split()
    if "End" in command:
        break
    elif "add" in command:
        wagon_numbers[-1] += int(command[1])
    elif "insert" in command:
        wagon_numbers[int(command[1])] += int(command[2])
    elif "leave" in command:
        wagon_numbers[int(command[1])] -= int(command[2])
print(wagon_numbers)
