number_loop = int(input())
counter = 0
for i in range(number_loop+1):
    for f in range(number_loop+1):
        for h in range(number_loop+1):
            if (i + f + h) == number_loop:
                counter += 1

print(counter)
