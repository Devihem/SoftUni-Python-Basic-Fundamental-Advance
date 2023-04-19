user_input = input()

all_used_letters_set = set()
all_used_letters_dict = dict()

for symbol in user_input:
    all_used_letters_set.add(symbol)

for symbol in all_used_letters_set:
    all_used_letters_dict[symbol] = (user_input.count(symbol))

[print(f"{key}: {all_used_letters_dict[key]} time/s") for key in sorted(all_used_letters_dict.keys())]
