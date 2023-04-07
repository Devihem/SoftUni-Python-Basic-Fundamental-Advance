neighborhood_list = [int(number) for number in input().split("@")]
cupid_position = 0
while True:

    system_input = input().split()
    command = system_input[0]

    if command == "Love!":
        neighborhood_list = [house for house in neighborhood_list if house > 0]
        print(f"Cupid's last position was {cupid_position}.")
        if len(neighborhood_list) == 0:
            print("Mission was successful.")
        else:
            print(f"Cupid has failed {len(neighborhood_list)} places.")
        break

    jump_length = int(system_input[1])
    cupid_position += jump_length
    if cupid_position >= len(neighborhood_list):
        cupid_position = 0

    if neighborhood_list[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")
    else:
        neighborhood_list[cupid_position] -= 2
        if neighborhood_list[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")
