loop = int(input())

sum_even = 0
sum_odd = 0

for i in range(0, loop):
    x = int(input())
    if i % 2 == 0:
        sum_even = sum_even + x
    elif i % 2 == 1:
        sum_odd = sum_odd + x

if sum_even == sum_odd:
    print("Yes")
    print(f"Sum = {sum_even}")
elif sum_even != sum_odd:
    print("No")
    print(f"Diff = {abs(sum_even - sum_odd)}")
