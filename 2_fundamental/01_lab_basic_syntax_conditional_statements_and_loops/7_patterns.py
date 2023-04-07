n = int(input())

for l1 in range(1, n*2):
    if l1 > n:
        print((n*2-l1)*"*")
    else:
        print(l1*"*")
