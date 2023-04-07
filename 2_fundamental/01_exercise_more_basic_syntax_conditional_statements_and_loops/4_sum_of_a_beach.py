input_string = str.lower(input())
count = 0
beach_word = ["fish", "water", "sun", "sand"]

for list_word in beach_word:
    count += input_string.count(list_word)

print(count)
