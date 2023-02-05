def swap_e_2_2(working_list: list, swap_index_1: int, swap_index_2: int):
    working_list[swap_index_1], working_list[swap_index_2] = working_list[swap_index_2], working_list[swap_index_1]
    return working_list


def multiply_e_2_2(working_list: list, multiply_index_1: int, multiply_index_2: int):
    working_list[multiply_index_1] *= working_list[multiply_index_2]
    return working_list


def decrease_e_2_2(working_list: list):
    working_list = [number - 1 for number in working_list]
    return working_list


list_with_numbers = [int(number) for number in input().split()]

while True:
    command = input().split()
    if command[0] == "end":
        list_with_numbers = [str(number) for number in list_with_numbers]
        print(', '.join(list_with_numbers))
        break

    elif command[0] == "swap":
        list_with_numbers = swap_e_2_2(list_with_numbers, int(command[1]), int(command[2]))

    elif command[0] == "multiply":
        list_with_numbers = multiply_e_2_2(list_with_numbers, int(command[1]), int(command[2]))

    elif command[0] == "decrease":
        list_with_numbers = decrease_e_2_2(list_with_numbers)
