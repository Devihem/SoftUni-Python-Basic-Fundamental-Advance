def numbers_searching(*numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    missing_number = None
    double_list_numbers = []
    for number in range(min_number, max_number):
        number_count = numbers.count(number)
        if number_count >= 2:
            double_list_numbers.append(number)
        elif number_count == 0:
            missing_number = number

    new_sorted_list = [missing_number, double_list_numbers]

    return new_sorted_list


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
