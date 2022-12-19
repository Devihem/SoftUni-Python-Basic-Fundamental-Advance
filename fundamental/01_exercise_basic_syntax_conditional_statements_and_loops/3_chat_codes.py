code_number_loop = int(input())

for number in range(0, code_number_loop):

    chat_number = int(input())

    if chat_number == 88:
        print("Hello")
    elif chat_number == 86:
        print("How are you?")
    elif chat_number < 88:
        print("GREAT!")
    elif chat_number > 88:
        print("Bye.")