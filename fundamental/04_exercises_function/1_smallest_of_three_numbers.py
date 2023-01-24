def smallest_of_3_int_4_1(number_1, number_2, number_3):
    list_with_ints = [number_1, number_2, number_3]
    return min(list_with_ints)


first_int = int(input())
second_int = int(input())
third_int = int(input())
print(smallest_of_3_int_4_1(first_int, second_int, third_int))