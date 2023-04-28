first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    'Add First': lambda numbers: [first_set.add(x) for x in numbers],
    'Add Second': lambda numbers: [second_set.add(x) for x in numbers],
    'Remove First': lambda numbers: [first_set.discard(x) for x in numbers],
    'Remove Second': lambda numbers: [second_set.discard(x) for x in numbers],
    'Check Subset': lambda numbers:
    print('True') if first_set.issubset(second_set) or second_set.issubset(first_set) else print('False')
}

for _ in range(int(input())):
    command = input().split()
    func = command[0] + ' ' + command[1]
    number_list = [int(x) for x in command[2:]]

    functions[func](number_list)

print(*(sorted(first_set)), sep=', ')
print(*(sorted(second_set)), sep=', ')
