def operate(operator: str, *numbers):
    def addition():
        result = 0
        for numb in numbers:
            result += numb
        return result

    def subtraction():
        result = numbers[0] * 2
        for numb in numbers:
            result -= numb
        return result

    def multiply():
        result = 1
        for numb in numbers:
            result *= numb
        return result

    def division():
        result = numbers[0] * numbers[0]
        for numb in numbers:
            result /= numb
        return result

    if operator == "+":
        return addition()

    elif operator == "-":
        return subtraction()

    elif operator == "*":
        return multiply()

    elif operator == "/":
        return division()


print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 3, 4))
