number1 = int(input())
number2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 == 0:
        result = 0
    else:
        result = number1 / number2
elif operator == "%":
    if number2 == 0:
        result = 0
    elif operator == "%":
        result = number1 % number2

if result % 2 == 0 and (operator == "+" or operator == "-" or operator == "*"):
    print(f"{number1} {operator} {number2} = {result} - even")

elif result % 2 == 1 and (operator == "+" or operator == "-" or operator == "*"):
    print(f"{number1} {operator} {number2} = {result} - odd")

if operator == "/" and number2 == 0:
    print(f"Cannot divide {number1} by zero")
elif operator == "/":
    print(f"{number1} {operator} {number2} = {result:.2f}")

if operator == "%" and number2 == 0:
    print(f"Cannot divide {number1} by zero")
elif operator == "%":
    print(f"{number1} {operator} {number2} = {result}")
