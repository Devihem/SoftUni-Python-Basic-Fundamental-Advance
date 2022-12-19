start_point = input()
end_point = input()

for x1 in range(int(start_point[0]), (int(end_point[0]) + 1)):
    for x2 in range(int(start_point[1]), int(end_point[1]) + 1):
        for x3 in range(int(start_point[2]), int(end_point[2]) + 1):
            for x4 in range(int(start_point[3]), int(end_point[3]) + 1):
                if x1 % 2 == 1:
                    if x2 % 2 == 1:
                        if x3 % 2 == 1:
                            if x4 % 2 == 1:
                                print(f"{x1}{x2}{x3}{x4}", end=" ")
