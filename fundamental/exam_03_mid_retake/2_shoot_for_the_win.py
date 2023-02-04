targets_list = [int(number) for number in input().split()]
count = 0
while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index in range(len(targets_list)):
        if targets_list[index] > -1:
            working_index = targets_list[index]
            targets_list[index] = -1
            count += 1
            for index_list, target in enumerate(targets_list):
                if target > -1:
                    if target > working_index:
                        targets_list[index_list] = target - working_index
                    else:
                        targets_list[index_list] = target + working_index

targets_list = [str(value) for value in targets_list]
print(f"Shot targets: {count} -> {' '.join(targets_list)}")
