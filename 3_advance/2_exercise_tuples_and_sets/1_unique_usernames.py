number_of_names = int(input())

names_set = {input() for _ in range(number_of_names)}

print('\n'.join(names_set))