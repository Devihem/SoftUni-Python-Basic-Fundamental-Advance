coded_password = input()

while True:

    command = input().split(" ")
    if command[0] == "Done":
        print(f"Your password is: {coded_password}")
        break

    # Command  TakeOdd
    elif command[0] == "TakeOdd":
        temporary_string = ""
        for index, symbol in enumerate(coded_password):
            if index % 2 == 1:
                temporary_string += symbol
        coded_password = temporary_string
        print(temporary_string)

    # Command Cut
    elif command[0] == "Cut":
        starting_index, sub_length = int(command[1]), int(command[2])
        cut_string = coded_password[starting_index:starting_index + sub_length]
        coded_password = coded_password.replace(cut_string, "", 1)
        print(coded_password)

    # Command Substitute
    elif command[0] == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in coded_password:
            coded_password = coded_password.replace(substring, substitute)
            print(coded_password)
        else:
            print("Nothing to replace!")