text_1 = input()
text_2 = input()

for char in range(0, len(text_2)):
    sample1 = text_2[:char+1:]
    sample2 = text_1[char+1::]
    if text_1[char] == text_2[char]:
        continue
    else:
        print(sample1+sample2)
