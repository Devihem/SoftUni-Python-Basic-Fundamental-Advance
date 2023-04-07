list_with_numbers = [int(number) for number in input().split(", ")]
positive_list = ", ".join([str(pos_num) for pos_num in list_with_numbers if pos_num >= 0])
negative_list = ", ".join([str(neg_num) for neg_num in list_with_numbers if neg_num < 0])
even_list = ", ".join([str(even_num) for even_num in list_with_numbers if even_num % 2 == 0])
odd_list = ", ".join([str(odd_num) for odd_num in list_with_numbers if odd_num % 2 == 1])
print(f"Positive: {positive_list}")
print(f"Negative: {negative_list}")
print(f"Even: {even_list}")
print(f"Odd: {odd_list}")
