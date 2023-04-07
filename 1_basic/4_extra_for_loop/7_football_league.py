stadium_capacity = int(input())
fans_loop = int(input())

a_seats = 0
b_seats = 0
v_seats = 0
g_seats = 0

for i in range(0, fans_loop):
    sector_fan = input()
    if sector_fan == "A":
        a_seats += 1
    elif sector_fan == "B":
        b_seats += 1
    elif sector_fan == "V":
        v_seats += 1
    elif sector_fan == "G":
        g_seats += 1

print(f"{(a_seats/fans_loop)*100:.2f}%")
print(f"{(b_seats/fans_loop)*100:.2f}%")
print(f"{(v_seats/fans_loop)*100:.2f}%")
print(f"{(g_seats/fans_loop)*100:.2f}%")
print(f"{((a_seats+b_seats+v_seats+g_seats)/stadium_capacity)*100:.2f}%")
