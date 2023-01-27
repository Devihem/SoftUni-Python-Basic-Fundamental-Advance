numbers_list = [int(number) for number in input().split(", ")]
even_number_index_list = [index for index, number in enumerate(numbers_list) if number%2 == 0]
print(even_number_index_list)
