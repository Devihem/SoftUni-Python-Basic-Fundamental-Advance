with open('words.txt', 'r') as words_doc:
    key_words_dict = {key: 0 for key in (words_doc.read().split())}

with open('input.txt', 'r') as read_doc:
    scan_text = [x.strip('-').strip('.').strip('?').strip(',') for x in (read_doc.read().split())]


for key in key_words_dict.keys():
    for word in scan_text:
        if key == word.lower():
            key_words_dict[key] += 1

print(key_words_dict)
sorted_count_word = sorted(key_words_dict.items(), key=lambda k: -k[1])
print(sorted_count_word)

with open('output', 'w') as output_file:
    for key, count in sorted_count_word:
        output_file.write(f"{key} - {count}\n")
