loop = int(input())

odd_sum = 0
odd_min = 1000000000.0
odd_max = -1000000000.0
even_sum = 0
even_min = 1000000000.0
even_max = -1000000000.0
even_flag = False
odd_flag = False

for i in range(1, loop+1):
    next_number = float(input())
    if i % 2 == 0:
        even_flag = True
        even_sum += next_number
        if even_max < next_number:
            even_max = next_number
        if even_min > next_number:
            even_min = next_number
    elif i % 2 == 1:
        odd_flag = True
        odd_sum += next_number
        if odd_max < next_number:
            odd_max = next_number
        if odd_min > next_number:
            odd_min = next_number

print(f"OddSum={odd_sum:.2f},")
if odd_flag == False:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_flag == False:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
