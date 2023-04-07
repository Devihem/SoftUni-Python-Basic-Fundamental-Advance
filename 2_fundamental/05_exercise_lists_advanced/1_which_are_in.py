key_word_list = input().split(", ")
all_word_list = input().split(", ")
key_word_list = [[key_word for word in all_word_list if key_word in word] for key_word in key_word_list]
new_key_words_list = [item[0] for item in key_word_list if len(item) > 0]
print(new_key_words_list)
