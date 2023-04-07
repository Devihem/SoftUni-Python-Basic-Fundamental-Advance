gift_list = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    command = command.split(" ")

    if "OutOfStock" in command:
        if command[1] in gift_list:
            for x in range(len(gift_list)):
                gift = gift_list[x]
                if command[1] == gift:
                    gift_list[x] = "None"

    elif "Required" in command:
        if len(gift_list) >= (int(command[2]) + 1) >= 0:
            gift_list[int(command[2])] = command[1]

    elif "JustInCase" in command:
        gift_list.pop()
        gift_list.append(command[1])

while "None" in gift_list:
    gift_list.remove("None")

print(*gift_list)