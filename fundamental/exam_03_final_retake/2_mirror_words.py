import re
mirror_words = []

text = input()
pattern = r"([#@])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
correct_words_match = re.findall(pattern, text)

for words_pair in correct_words_match:
    if words_pair[1] == words_pair[2][::-1]:
        mirror_words.append(f"{words_pair[1]} <=> {words_pair[2]}")

if len(correct_words_match) < 1:
    print("No word pairs found!")
else:
    print(f"{len(correct_words_match)} word pairs found!")

if len(mirror_words) < 1:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_words))
