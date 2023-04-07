string_1, string_2 = input().split(" ")
final_sum = 0
counter = 0
while counter + 1 <= len(string_1) or counter + 1 <= len(string_2):
    if counter < len(string_1):
        string_1_value = ord(string_1[counter])
    else:
        string_1_value = 1

    if counter < len(string_2):
        string_2_value = ord(string_2[counter])
    else:
        string_2_value = 1
    final_sum += string_1_value * string_2_value
    counter += 1
print(final_sum)
