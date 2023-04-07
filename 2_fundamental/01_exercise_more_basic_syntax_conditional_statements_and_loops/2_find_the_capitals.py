random_word = input()
list_with_uppers = []
for order, letter in enumerate(random_word):
    if str(letter).isupper():
        list_with_uppers.append(order)

print(list_with_uppers)
