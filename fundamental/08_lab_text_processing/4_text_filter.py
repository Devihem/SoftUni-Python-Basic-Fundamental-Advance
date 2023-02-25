banned_words_list = input().split(", ")
text_for_reformat = input()

for word in banned_words_list:
    while word in text_for_reformat:
        text_for_reformat = text_for_reformat.replace(word, len(word) * "*")

print(text_for_reformat)
