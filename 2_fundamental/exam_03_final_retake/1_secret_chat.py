coded_text = input()

while True:

    command = input().split(":|:")
    if command[0] == "Reveal":
        print(f"You have a new text message: {coded_text}")
        break

    # Command Insert
    elif command[0] == "InsertSpace":
        index = int(command[1])
        coded_text = coded_text[:index] + " " + coded_text[index:]
        print(coded_text)
    # Command Reverse
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in coded_text:
            sub_star_index = coded_text.index(substring)
            sub_reversed = substring[::-1]
            coded_text = coded_text[:sub_star_index] + coded_text[sub_star_index + len(sub_reversed):] + sub_reversed
            print(coded_text)
        else:
            print("error")

    # Command ChangeALL
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        coded_text = coded_text.replace(substring, replacement)
        print(coded_text)
