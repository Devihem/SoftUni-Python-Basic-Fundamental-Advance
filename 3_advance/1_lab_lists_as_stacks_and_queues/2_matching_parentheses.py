input_math_line = input()
parentheses_stack = []

index_counter = -1
for symbol in input_math_line:
    index_counter += 1
    if symbol == "(":
        parentheses_stack.append(index_counter)
    elif symbol == ")":
        starting_index = parentheses_stack.pop()
        end_index = index_counter
        print(input_math_line[starting_index:index_counter+1])