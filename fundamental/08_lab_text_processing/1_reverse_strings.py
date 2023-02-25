while True:
    command = input()
    if command == "end":
        break
    word = command
    reversed_word = ''.join(list(reversed(word)))
    print(f"{word} = {reversed_word}")
