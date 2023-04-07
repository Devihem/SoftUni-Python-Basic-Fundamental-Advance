my_stack = list(input())
final_stack = []

for symbol in range(len(my_stack)):
    pop_symbol = my_stack.pop()
    final_stack.append(pop_symbol)

print(''.join(final_stack))
