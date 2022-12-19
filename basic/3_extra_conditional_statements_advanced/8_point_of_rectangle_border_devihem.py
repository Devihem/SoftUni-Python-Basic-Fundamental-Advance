x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if x1 == x or x2 == x or y1 == y or y2 == y:
    print("Border")
elif x1 <= x <= x2 and y1 <= y <= y2:
    print("Inside")
else:
    print("Outside")
