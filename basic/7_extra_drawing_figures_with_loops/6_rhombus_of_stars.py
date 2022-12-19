size = int(input())
k = size
filler_3 = 0

for up_row in range(1, size+1):
    for filler_1 in range(1, k):
        print(" ",end="")
    k = k - 1
    for filler_2 in range(0, up_row):
        print("* ", end="")
    print()
for down_row in range(1, size):
    for filler_3 in range(1, down_row+1):
        print(" ", end="")
    for filler_4 in range(size-filler_3, 0, -1):
        print("* ", end="")
    print()