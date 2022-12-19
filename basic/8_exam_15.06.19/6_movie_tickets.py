a1 = int(input())
a2 = int(input())
n = int(input())

for symb1 in range(a1, a2):
    symb4 = symb1
    for symb2 in range(1, n):
        for symb3 in range(1, int(n/2)):
            if symb4 % 2 == 1 and (symb3 + symb4 + symb2) % 2 == 1:
                print(f"{chr(symb1)}-{symb2}{symb3}{symb4}")
