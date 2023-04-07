import string

command = ""
secret_word = ""
password_word = ""
counter_c = 0
counter_n = 0
counter_o = 0
print_word = ""

while command != "End":
    if "c" in password_word and "n" in password_word and "o" in password_word:
        print_word += secret_word
        password_word = ""
        secret_word = ""
        counter_c = 0
        counter_o = 0
        counter_n = 0

    command = input()
    if command in string.ascii_letters:

        if command == "c" and counter_c < 1:
            counter_c += 1
            password_word += command
        elif command == "o" and counter_o < 1:
            counter_o += 1
            password_word += command
        elif command == "n" and counter_n < 1:
            counter_n += 1
            password_word += command
        else:
            secret_word += command
print(print_word)
