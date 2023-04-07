input_words = input().split(" ")
final_string = ""

for word in input_words:
    for _ in range(len(word)):
        final_string += word

print(final_string)
