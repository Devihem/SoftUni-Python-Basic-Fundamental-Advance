new_list = [char for char in list(input()) if char not in ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']]
print(*new_list, sep="")
