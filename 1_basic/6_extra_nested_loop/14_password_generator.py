n_number = int(input())
l_number = int(input())

for x1 in range(1, n_number + 1 ):
    for x2 in range(1, n_number + 1):
        for x3 in range(ord("a"), ord("a")+l_number):
            for x4 in range(ord("a"), ord("a")+l_number):
                for x5 in range(1, n_number+1):
                    if x5 <= x1 or x5 <= x2:
                        continue
                    else:
                        print(f"{x1}{x2}{chr(x3)}{chr(x4)}{x5}", end=" ")
