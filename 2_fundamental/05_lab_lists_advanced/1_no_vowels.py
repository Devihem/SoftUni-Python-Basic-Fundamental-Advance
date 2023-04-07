new_list = [char for char in list(input()) if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(new_list))
