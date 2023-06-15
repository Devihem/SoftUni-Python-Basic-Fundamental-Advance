from collections import deque

vowels_list = deque(input().split())
consonants_list = deque(input().split())

founded_word_flag = False
unlocked_letters = []
key_words = [
    'rose',
    'tulip',
    'lotus',
    'daffodil'
]
while vowels_list and consonants_list:

    current_vowel = vowels_list.popleft()
    current_consonant = consonants_list.pop()

    for check_word in key_words:
        if current_vowel in check_word:
            unlocked_letters.append(current_vowel)
        if current_consonant in check_word:
            unlocked_letters.append(current_consonant)
        for letter_by_letter in check_word:
            if letter_by_letter not in unlocked_letters:
                break
        else:
            founded_word_flag = True

        if founded_word_flag:
            print(f"Word found: {check_word}")
            break
    if founded_word_flag:
        break

else:
    print("Cannot find any word!")

if vowels_list:
    print("Vowels left: ", end='')
    print(*vowels_list, sep=' ')

if consonants_list:
    print("Consonants left: ", end='')
    print(*consonants_list, sep=' ')
