def factorial_4_12(int_number=10):
    total_sum = 1
    for number in range(1, int_number + 1):
        total_sum *= number
    return total_sum


number_1 = int(input())
number_2 = int(input())
number_1_factorial = factorial_4_12(number_1)
number_2_factorial = factorial_4_12(number_2)
result = number_1_factorial / number_2_factorial
print(f"{result:.2f}")
