iteration_count = int(input())
flag_open_bracket = False
flag_closing_bracket = False
for new_line in range(iteration_count):
    char = input()
    if flag_open_bracket and flag_closing_bracket:
        flag_open_bracket = False
        flag_closing_bracket = False
    if char == "(":
        if not flag_open_bracket and not flag_closing_bracket:
            flag_open_bracket = True
            continue
        else:
            print("UNBALANCED")
            break
    elif char == ")":
        if flag_open_bracket and not flag_closing_bracket:
            flag_closing_bracket = True
            continue
        else:
            print("UNBALANCED")
            break
else:
    print("BALANCED")
