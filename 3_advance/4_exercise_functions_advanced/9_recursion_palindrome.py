def palindrome(word: str, first_word):
    if first_word == 0:
        first_word = word

    if word[0] == word[-1]:
        word = word[1:-1]
        if len(word) > 1:
            palindrome(word, 0)
        return f"{first_word} is a palindrome"
    return f"{first_word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter retep", 0))
print(palindrome("avvvvvva", 0))
print(palindrome(" ", 0))
