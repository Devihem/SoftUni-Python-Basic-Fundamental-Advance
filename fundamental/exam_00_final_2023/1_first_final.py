coded_string = input()

while True:

    data_input = input().split(" ")
    command = data_input[0]

    if command == "Abracadabra":
        break

    elif command == "Abjuration":
        coded_string = coded_string.upper()
        print(coded_string)

    elif command == "Necromancy":
        coded_string = coded_string.lower()
        print(coded_string)

    elif command == "Illusion":
        index = int(data_input[1])
        letter = data_input[2]
        if 0 <= index < len(coded_string):
            coded_string = coded_string[:index] + letter + coded_string[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")

    elif command == "Divination":
        first_sub = data_input[1]
        second_sub = data_input[2]
        if first_sub in coded_string:
            coded_string = coded_string.replace(first_sub, second_sub)
            print(coded_string)

    elif command == "Alteration":
        substring = data_input[1]
        if substring in coded_string:
            coded_string = coded_string.replace(substring, "", 1)
            print(coded_string)

    else:
        print("The spell did not work!")
