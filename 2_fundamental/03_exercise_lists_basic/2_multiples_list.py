factor = int(input())
counts = int(input())
refactored_number = 0
list_numbers = []
for step in range(1, counts + 1):
    refactored_number = step * factor
    list_numbers.append(refactored_number)
else:
    print(list_numbers)

