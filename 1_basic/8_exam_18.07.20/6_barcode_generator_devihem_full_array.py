start_point = int(input())
end_point = int(input())

for i in range(start_point, end_point+1):
    i_str = str(i)
    x1 = int(i_str[3])
    x2 = int(i_str[2])
    x3 = int(i_str[1])
    x4 = int(i_str[0])
    if x1 % 2 == 1:
        if x2 % 2 == 1:
            if x3 % 2 == 1:
                if x4 % 2 == 1:
                    print(i, end=" ")