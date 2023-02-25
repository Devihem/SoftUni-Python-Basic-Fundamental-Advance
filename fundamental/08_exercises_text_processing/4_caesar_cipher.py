random_string = input()
final_coded_string = ""

for char in list(random_string):
    final_coded_string += chr((ord(char) + 3))

print(final_coded_string)
