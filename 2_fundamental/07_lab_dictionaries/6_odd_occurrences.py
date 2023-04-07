words_dict = {}
words_list = input().split()
for word in words_list:
    if word.lower() not in words_dict:
        words_dict[word.lower()] = 1
    else:
        words_dict[word.lower()] += 1

[print(x, end=" ") for x in words_dict if words_dict[x] % 2 == 1]
