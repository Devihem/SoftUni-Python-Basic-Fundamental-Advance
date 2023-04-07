number_loop = int(input())
counter = 0
total_x = 0
while counter < number_loop:
    x = int(input())
    total_x += x
    counter += 1
print(f"{total_x/counter:.2f}")
