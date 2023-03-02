message_key = input().split()
treasure = ""
coordinates = ""

while True:
    command = input()
    if command == "find":
        break
    fixed_string = ""
    key_counter = 0
    for char in command:
        fixed_string += chr(ord(char) - int(message_key[key_counter]))
        key_counter += 1
        if key_counter == len(message_key):
            key_counter = 0

    # Finding the start/end index in the string , based on & - Treasure
    treasure_starting_index = (fixed_string.index("&")) + 1
    treasure_final_index = (fixed_string.index("&", treasure_starting_index))
    treasure = fixed_string[treasure_starting_index: treasure_final_index]

    # Finding the start/end index in the string, based on < , > - Coordinates
    coordinates_starting_index = (fixed_string.index("<")) + 1
    coordinates_final_index = (fixed_string.index(">", coordinates_starting_index))
    coordinates = fixed_string[coordinates_starting_index: coordinates_final_index]

    print(f"Found {treasure} at {coordinates}")
