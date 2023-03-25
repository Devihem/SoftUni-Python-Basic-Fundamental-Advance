number_of_pieces_to_add = int(input())
music_dict = {}
for piece_add in range(number_of_pieces_to_add):
    piece, composer, key = input().split("|")
    if piece not in music_dict.keys():
        music_dict[piece] = [composer, key]

while True:

    command = input().split("|")
    if command[0] == "Stop":
        break

    # Command - ADD
    elif command[0] == "Add":
        piece, composer, key = command[1], command[2], command[3]
        if piece in music_dict.keys():
            print(f"{piece} is already in the collection!")
        else:
            music_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    # Command - REMOVE
    elif command[0] == "Remove":
        piece = command[1]
        if piece in music_dict.keys():
            music_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    # Command = CHANGE KEY
    elif command[0] == "ChangeKey":
        piece, new_key = command[1], command[2]
        if piece in music_dict.keys():
            music_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

[print(f"{dict_key} -> Composer: {music_dict[dict_key][0]}, Key: {music_dict[dict_key][1]}") for dict_key in music_dict.keys()]
