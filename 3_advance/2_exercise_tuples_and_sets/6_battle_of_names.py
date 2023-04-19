odd_set = set()
even_set = set()

for row in range(int(input())):
    name = input()
    ascii_sum = 0
    for symbol in name:
        ascii_sum += ord(symbol)
    ascii_sum = int(ascii_sum / (row + 1))
    if ascii_sum % 2 == 1:
        odd_set.add(ascii_sum)
    else:
        even_set.add(ascii_sum)

if sum(even_set) == sum(odd_set):
    print(*(odd_set.union(even_set)), sep=', ')
elif sum(even_set) < sum(odd_set):
    print(*(odd_set.difference(even_set)), sep=', ')
elif sum(even_set) > sum(odd_set):
    print(*(odd_set.symmetric_difference(even_set)), sep=', ')
