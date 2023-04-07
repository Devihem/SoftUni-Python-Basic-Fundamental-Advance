starting_input = input()
max_number = starting_input

while starting_input != "Stop":
    loop_input = int(starting_input)
    if int(max_number) < loop_input:
        max_number = loop_input
    else:
        starting_input = input()

print(max_number)
