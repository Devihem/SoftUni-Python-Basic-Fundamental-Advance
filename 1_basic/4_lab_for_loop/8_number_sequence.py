loops = int(input())
x = int(input())
y = x
z = x

for i in range(0, loops-1):
    x = int(input())
    if y > x:
        y = x
    elif z < x:
        z = x

if loops == 1:
    print(f"Max number: {x}")
    print(f"Min number: {x}")
else:
    print(f"Max number: {z}")
    print(f"Min number: {y}")