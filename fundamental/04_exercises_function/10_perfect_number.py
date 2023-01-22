def aliquot_sum_of_integer_4_9(input_number):
    total_sum = 0
    if input_number < 0:
        return "It's not so perfect."

    for number in range(1, input_number):
        if input_number % number == 0:
            total_sum += number
    if total_sum == input_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number_input = int(input())
print(aliquot_sum_of_integer_4_9(number_input))

