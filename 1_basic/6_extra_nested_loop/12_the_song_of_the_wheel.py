number_m = int(input())
password_counter = 0
password = ""

for x1 in range(1, 9+1):
    pass
    for x2 in range(1, 9 + 1):
        if x2 <= x1:
            continue
        for x3 in range(1, 9 + 1):
            pass
            for x4 in range(1, 9 + 1):
                if x4 >= x3:
                    continue
                if number_m == ((x1*x2) + (x3*x4)):
                    password_counter += 1
                    print(f"{x1}{x2}{x3}{x4} ", end="")
                    if password_counter == 4:
                        password = str(x1)+str(x2)+str(x3)+str(x4)
print()
if password_counter >= 4:
    print(f"Password: {password}")
else:
    print("No!")