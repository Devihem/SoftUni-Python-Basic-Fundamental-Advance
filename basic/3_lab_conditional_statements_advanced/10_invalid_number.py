number = int(input())

checking = 100 <= number <= 200 or number == 0

if not checking:
    print("invalid")
