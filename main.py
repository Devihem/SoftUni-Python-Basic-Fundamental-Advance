new_dict = {'Simo': 200, 'Zeter': 550, 'Peter': 550, 'George': 300, 'Zimo': 200, 'Aimo': 200, 'Mariya': 600}
print(new_dict.items())

sorted_new_dict = sorted(new_dict.items(), key=lambda k: (-k[1], k[0]))

print(sorted_new_dict)