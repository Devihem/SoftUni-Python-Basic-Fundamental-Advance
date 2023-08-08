max_number = int(input())
for number_i in range(1, max_number + 1):
    if number_i % 3 == 0 and number_i % 5 == 0:
        print("FizzBuzz")
    elif number_i % 3 == 0:
        print("Fizz")
    elif number_i % 5 == 0:
        print("Buzz")
    else:
        print(number_i)
