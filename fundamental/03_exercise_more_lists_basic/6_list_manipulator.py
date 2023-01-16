list_of_numbers = list(input().split())

while True:
    command = input().split()

    if command[0] == "end":
        break

    elif command[0] == "exchange":
        if int(command[1]) >= len(list_of_numbers) or int(command[1]) < 0:
            print("Invalid index")
        else:
            working_list_a = list_of_numbers[:int(command[1]) + 1]
            working_list_b = list_of_numbers[int(command[1]) + 1:]
            list_of_numbers = working_list_b + working_list_a

    elif command[0] == "max":
        working_list_a = sorted(list_of_numbers, key=int)
        working_value_a = "No matches"
        if command[1] == "even":
            for number in list(reversed(working_list_a)):
                if int(number) % 2 == 0:
                    working_value_a = number
                    break
        elif command[1] == "odd":
            for number in list(reversed(working_list_a)):
                if int(number) % 2 == 1 :
                    working_value_a = number
                    break

        if working_value_a != "No matches":
            counter = int(len(list_of_numbers))
            for min_max_even_number in list(reversed(list_of_numbers)):
                counter -= 1
                if min_max_even_number == working_value_a:
                    print(counter)
                    break
        else:
            print(working_value_a)

    elif command[0] == "min":
        working_list_a = sorted(list_of_numbers, key=int)
        working_value_a = "No matches"
        if len(list_of_numbers) < 1:
            print(working_value_a)
            continue
        elif command[1] == "even":
            for number in working_list_a:
                if int(number) % 2 == 0:
                    working_value_a = number
                    break
        elif command[1] == "odd":
            for number in working_list_a:
                if int(number) % 2 == 1 :
                    working_value_a = number
                    break
        if working_value_a != "No matches":
            counter = int(len(list_of_numbers))
            for min_max_even_number in list(reversed(list_of_numbers)):
                counter -= 1
                if min_max_even_number == working_value_a:
                    print(counter)
                    break
        else:
            print(working_value_a)
            working_value_a = 0

    elif command[0] == "first":
        working_list_a = []
        if len(list_of_numbers) < 1 or int(command[1]) > len(list_of_numbers):
            print("Invalid count")
            continue
        elif command[2] == "even":
            for number in list_of_numbers:
                if int(number) % 2 == 0:
                    if len(working_list_a) == int(command[1]):
                        break
                    else:
                        working_list_a.append(number)
        elif command[2] == "odd":
            for number in list_of_numbers:
                if int(number) % 2 == 1:
                    if len(working_list_a) == int(command[1]):
                        break
                    else:
                        working_list_a.append(number)
        print("[", end="")
        print(*working_list_a, sep=", ", end="")
        print("]")

    elif command[0] == "last":
        working_list_a = []
        if len(list_of_numbers) < 1 or int(command[1]) > len(list_of_numbers):
            print("Invalid count")
            continue
        elif command[2] == "even":
            for number in list(reversed(list_of_numbers)):
                if int(number) % 2 == 0:
                    if len(working_list_a) == int(command[1]):
                        break
                    else:
                        working_list_a.append(number)
        elif command[2] == "odd":
            for number in list(reversed(list_of_numbers)):
                if int(number) % 2 == 1:
                    if len(working_list_a) == int(command[1]):
                        break
                    else:
                        working_list_a.append(number)
        working_list_b = list(reversed(working_list_a))
        print("[", end="")
        print(*working_list_b, sep=", ", end="")
        print("]")

print("[", end="")
print(*list_of_numbers, sep=", ", end="")
print("]")
