x1 = int(input())
x2 = int(input())
magic_number = int(input())
magic_number_flag = False
counter = 0

for i in range(x1, x2+1):
    if magic_number_flag:
        break
    for f in range(x1, x2+1):
        counter += 1
        if (f + i) == magic_number:
            print(f"Combination N:{counter} ({i} + {f} = {magic_number})")
            magic_number_flag = True
            break
else:
    if not magic_number_flag:
        print(f"{counter} combinations - neither equals {magic_number}")
