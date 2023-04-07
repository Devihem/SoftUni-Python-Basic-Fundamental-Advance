key_number = int(input())
number_of_letters = int(input())
secret_message = ""
for letter in range(number_of_letters):
    new_letter = input()
    secret_message += chr(ord(new_letter) + key_number)

print(secret_message)