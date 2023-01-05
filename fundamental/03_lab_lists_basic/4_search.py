number_of_words = int(input())
key_word = input()
text_list = []
text_list_filtered = []
for new_word in range(0, number_of_words):
    new_word_input = input()
    text_list.append(new_word_input)

for item in text_list:
    if key_word in item:
        text_list_filtered.append(item)

print(text_list)
print(text_list_filtered)
