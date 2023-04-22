first_set = set(input().split())
second_set = set(input().split())


for _ in range(int(input())):
    command = input().split()

    if command[0] == "Add":
        add_list = command[2:]
        if command[1] == "First":
            first_set = first_set.union(add_list)
        elif command[1] == "Second":
            second_set = second_set.union(add_list)

    elif command[0] == "Remove":
        remove_list = command[2:]
        if command[1] == "First":
            first_set = first_set.difference(remove_list)
        elif command[1] == "Second":
            second_set = second_set.difference(remove_list)

    elif command[0] == "Check":
        subset_list_check = [first_set.issubset(second_set), second_set.issubset(first_set)]
        if True in subset_list_check:
            print("True")
        else:
            print("False")

print(', '.join(sorted(first_set)))
print(', '.join(sorted(second_set)))
