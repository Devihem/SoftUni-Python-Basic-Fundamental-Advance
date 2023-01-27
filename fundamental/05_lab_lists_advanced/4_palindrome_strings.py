words_list = [word for word in input().split() if word == word[::-1]]
keyword_user = input()
key_word_count = [+1 for keyword in words_list if keyword == keyword_user]
print(words_list)
print(f"Found palindrome {sum(key_word_count)} times")
