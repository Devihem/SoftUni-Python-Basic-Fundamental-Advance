list_with_numbers = list(map(float, input().split(" ")))
list_with_numbers = [abs(num) for num in list_with_numbers]
print(list_with_numbers)