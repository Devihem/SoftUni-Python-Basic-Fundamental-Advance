loop = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0, loop):
    x = int(input())
    if x < 200:
        p1 += 1
    elif 200 <= x < 400:
        p2 += 1
    elif 400 <= x < 600:
        p3 += 1
    elif 600 <= x < 800:
        p4 += 1
    elif 800 <= x <= 1000 :
        p5 += 1

print(f"{(p1/loop)*100:.2f}%")
print(f"{(p2/loop)*100:.2f}%")
print(f"{(p3/loop)*100:.2f}%")
print(f"{(p4/loop)*100:.2f}%")
print(f"{(p5/loop)*100:.2f}%")