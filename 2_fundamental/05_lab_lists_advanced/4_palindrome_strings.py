words_list = [word for word in input().split() if word == word[::-1]]
keyword = input()
print(words_list)
print(f"Found palindrome {words_list.count(keyword)} times")
