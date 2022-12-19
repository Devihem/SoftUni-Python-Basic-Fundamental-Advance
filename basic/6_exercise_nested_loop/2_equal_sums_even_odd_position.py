wtf_1 = int(input())
wtf_2 = int(input())
counter = 0
even = 0
odd = 0
for i in range(wtf_1, wtf_2+1):
    i = str(i)
    for f in reversed(i):
        counter += 1
        if counter % 2 == 1:
            odd += int(f)
        elif counter % 2 == 0:
            even += int(f)
    if even == odd:
        print(i, end=" ")
    even = 0
    odd = 0
