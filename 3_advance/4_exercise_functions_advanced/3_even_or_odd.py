def even_odd(*numbers_and_command):
    def command_even():
        even_numbs = [x for x in numbers if x % 2 == 0]
        return even_numbs

    def command_odd():
        odd_numbs = [x for x in numbers if x % 2 == 1]
        return odd_numbs

    *numbers, command = numbers_and_command

    if command == "even":
        return command_even()
    elif command == "odd":
        return command_odd()


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
