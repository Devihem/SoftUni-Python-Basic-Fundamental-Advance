def pass_validation_4_9(string):
    pass_length = pass_length_validator_4_9_a(string)
    pass_letters_digits_only = pass_letters_digits_letters_only_4_9_b(string)
    pass_min_2_digit = pass_min_2_digit_4_9_c(string)
    if not pass_length:
        print("Password must be between 6 and 10 characters")
    if not pass_letters_digits_only:
        print("Password must consist only of letters and digits")
    if not pass_min_2_digit:
        print("Password must have at least 2 digits")
    if pass_length and pass_letters_digits_only and pass_min_2_digit:
        print("Password is valid")


def pass_length_validator_4_9_a(string):
    if 6 <= len(string) <= 10:
        return True
    return False


def pass_letters_digits_letters_only_4_9_b(string):
    if string.isalnum():
        return True
    return False


def pass_min_2_digit_4_9_c(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    if count >= 2:
        return True
    return False


user_input_password = input()
pass_validation_4_9(user_input_password)
