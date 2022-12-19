best_word = 0
best_power = 0
total_score = 0
while True:
    word = input()
    if word == "End of words":
        break
    for i, x in enumerate(word):
        total_score += ord(x)

    if word[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
        total_score = total_score * len(word)
    else:
        total_score = total_score / len(word)

    if best_power < total_score:
        best_power = total_score
        best_word = word
    total_score = 0
print(f"The most powerful word is {best_word} - {best_power}" )
