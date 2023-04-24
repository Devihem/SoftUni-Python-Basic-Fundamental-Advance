first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())


for _ in range(int(input())):
    command = input().split()

    if command[0] == "Add":
        add_list = [int(x) for x in command[2:]]
        if command[1] == "First":
            first_set = first_set.union(add_list)
        elif command[1] == "Second":
            second_set = second_set.union(add_list)

    elif command[0] == "Remove":
        remove_list = [int(x) for x in command[2:]]
        if command[1] == "First":
            first_set = first_set.difference(remove_list)
        elif command[1] == "Second":
            second_set = second_set.difference(remove_list)

    elif command[0] == "Check":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")

print(*(sorted(first_set)), sep=', ')
print(*(sorted(second_set)), sep=', ')
