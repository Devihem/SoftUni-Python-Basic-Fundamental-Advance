loop = int(input())
left_sum = 0
right_sum = 0

for i in range(0, loop*2):
    if i < loop:
        left_sum = int(input()) + left_sum
    elif i >= loop:
        right_sum = int(input()) + right_sum
if right_sum == left_sum:
    print(f"Yes, sum = {left_sum}")
elif right_sum != left_sum:
    print(f"No, diff = {abs(left_sum-right_sum)}")
