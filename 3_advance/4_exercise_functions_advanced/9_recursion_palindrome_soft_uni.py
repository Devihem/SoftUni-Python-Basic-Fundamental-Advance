# def palindrome(word: str, odd_even_index):
#     result = ''
#     if len(word) % 2 == 0:
#         odd_even_index = 0
#     else:
#         odd_even_index = 1
#     print(word)
#     print(word[0], word[-1])
#     if word[0] == word[-1]:
#         word = word[1:-1]
#         print(word, odd_even_index)
#         print(len(word) == 1 and odd_even_index == 1)
#         if (len(word) == 0) or (len(word) == 1 and odd_even_index == 1):
#             print("here")
#             result = f"{word} is a palindrome"
#             return result
#         esel:
#             palindrome(word, odd_even_index)
#
#     return f"{word} is not a palindrome"
#
#
# print(palindrome("abcba", 0))
# # print(palindrome("peter retep", 0))
# # print(palindrome("avvvvvva", 0))
# # print(palindrome("  ", 0))
