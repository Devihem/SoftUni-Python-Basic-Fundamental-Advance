def add_oper(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a ** b


def calculate(user_input: str):
    number_1, operation, number_2 = user_input.split(' ')
    number_1 = float(number_1)
    number_2 = float(number_2)

    pattern = {
        '+': add_oper,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power,
    }

    return pattern[operation](number_1, number_2)
