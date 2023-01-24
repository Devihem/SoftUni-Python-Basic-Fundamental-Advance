digit_list = list(map(int, list((input()))))
odd_sum = sum(list(filter(lambda odd_number: odd_number % 2 == 1, digit_list)))
even_sum = sum(list(filter(lambda even_number: even_number % 2 == 0 and even_number != 0, digit_list)))
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
