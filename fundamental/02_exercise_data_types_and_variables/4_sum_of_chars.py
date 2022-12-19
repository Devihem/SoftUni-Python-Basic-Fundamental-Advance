loop_iterations = int(input())
total_sum = 0
for step in range(loop_iterations):
    new_character = input()
    total_sum += ord(new_character)
print(f"The sum equals: {total_sum}")
