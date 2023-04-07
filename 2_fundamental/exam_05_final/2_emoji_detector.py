import re

cool_threshold = 1
cool_emoji_list = []
basic_emoji_list = []
cool_text = input()

pattern_threshold = r"\d{1}"
pattern_emojis = r"(\:\:|\*\*)([A-Z][a-z]{2,})\1"

match_threshold_digits = re.findall(pattern_threshold, cool_text)
match_valid_emojis = re.findall(pattern_emojis, cool_text)

for digit in match_threshold_digits:
    cool_threshold *= int(digit)

for emoji in match_valid_emojis:
    current_score = 0
    for symbol in emoji[1]:
        current_score += ord(symbol)
    if current_score >= cool_threshold:
        cool_emoji_list.append(emoji[0] + emoji[1] + emoji[0])
    else:
        basic_emoji_list.append(emoji[0] + emoji[1] + emoji[0])
print(f"Cool threshold: {cool_threshold}")
print(f"{len(cool_emoji_list) + len(basic_emoji_list)} emojis found in the text. The cool ones are:")
[print(f"{print_final_emoji}") for print_final_emoji in cool_emoji_list]
