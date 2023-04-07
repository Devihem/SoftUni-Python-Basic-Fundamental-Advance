travel_text = input()

while True:

    command = input().split(":")

    if command[0] == "Travel":
        print(f"Ready for world tour! Planned stops: {travel_text}")
        break

    # Command - ADD
    elif command[0] == "Add Stop":
        index, string = int(command[1]), command[2]
        if len(travel_text) > index >= 0:
            travel_text = travel_text[:index] + string + travel_text[index:]
        print(travel_text)

    # Command - REMOVE
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index < len(travel_text) and 0 <= end_index < len(travel_text) and start_index <= end_index:
            travel_text = travel_text[:start_index] + travel_text[end_index + 1:]
        print(travel_text)

    # Command - SWITCH
    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in travel_text:
            travel_text = travel_text.replace(old_string, new_string)
        print(travel_text)
