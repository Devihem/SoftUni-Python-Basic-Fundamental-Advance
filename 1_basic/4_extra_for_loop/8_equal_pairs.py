pairs_loop = int(input())

x = int(input())
y = int(input())
z = x + y
flag = True
max_diff = 0
for i in range(0, pairs_loop-1):
    z = x + y
    x = int(input())
    y = int(input())
    if z != (x + y):
        flag = False
        diff = abs(z-(x+y))
        if diff > max_diff:
            max_diff = diff
if flag == True:
    print(f"Yes, value={z}")
elif flag == False:
    print(f"No, maxdiff={max_diff}")
