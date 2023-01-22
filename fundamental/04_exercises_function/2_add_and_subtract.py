def sum_numbers_4_2(d_number_1, d_number_2):
    return d_number_1 + d_number_2


def subtract_4_2(d_number_1, d_number_2):
    return d_number_1 - d_number_2


first_int = int(input())
second_int = int(input())
third_int = int(input())

sum_result = sum_numbers_4_2(first_int, second_int)
subtract_result = subtract_4_2(sum_result, third_int)
print(subtract_result)
