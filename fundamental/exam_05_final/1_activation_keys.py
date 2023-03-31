raw_key = input()

while True:

    command = input().split(">>>")
    if command[0] == "Generate":
        print(f"Your activation key is: {raw_key}")
        break

    # Command - CONTAINS
    elif command[0] == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    # Command - FLIP
    elif command[0] == "Flip":
        action = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if action == "Upper":
            raw_key = raw_key[:start_index] + raw_key[start_index:end_index].upper() + raw_key[end_index:]
        elif action == "Lower":
            raw_key = raw_key[:start_index] + raw_key[start_index:end_index].lower() + raw_key[end_index:]
        print(raw_key)

    # Command - SLICE
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)
        pass
