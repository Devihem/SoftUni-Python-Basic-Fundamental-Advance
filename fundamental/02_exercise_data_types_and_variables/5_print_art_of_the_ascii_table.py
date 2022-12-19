starting_range = int(input())
final_range = int(input())

for digit in range(starting_range, final_range+1):
    print(chr(digit), end=" ")
