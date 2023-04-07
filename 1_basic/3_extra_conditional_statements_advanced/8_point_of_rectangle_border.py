x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if (x1 == x or x2 == x) and y1 <= y <= y2:
    print("Border")
elif (y2 == y or y1 == y) and x1 <= x <= x2:
    print("Border")
else:
    print("Inside / Outside")
