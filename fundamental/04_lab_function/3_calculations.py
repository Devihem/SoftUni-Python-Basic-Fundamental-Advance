def calculator_4_3(number1, number2, str_operator):
    if str_operator == "multiply":
        return number1 * number2
    elif str_operator == "divide":
        return number1 / number2
    elif str_operator == "add":
        return number1 + number2
    elif str_operator == "subtract":
        return number1 - number2


operator = input()
first_number = int(input())
second_number = int(input())
print(calculator_4_3(first_number, second_number, operator))
