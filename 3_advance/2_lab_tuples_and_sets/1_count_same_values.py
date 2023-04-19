new_input = [float(x) for x in input().split()]
new_set = set()
for new_number in new_input:
    new_set.add(new_number)

print(new_set)
new_dict = {number: new_input.count(number) for number in new_set}
print(new_set)
print(new_dict)
