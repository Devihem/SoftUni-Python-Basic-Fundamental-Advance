control_word = input()
random_string = input()

while control_word in random_string:
    random_string = random_string.replace(control_word, "")
print(random_string)
