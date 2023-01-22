def list_check_for_palindromes_4_8(list_with_data):
    final_list = []
    for item in list_with_data:
        if item == item[::-1]:
            print("True")
        else:
            print("False")


new_list_with_digits = input().split(", ")
list_check_for_palindromes_4_8(new_list_with_digits)
