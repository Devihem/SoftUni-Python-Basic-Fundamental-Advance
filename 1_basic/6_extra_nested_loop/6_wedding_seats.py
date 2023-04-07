last_sector = input()
rows_sector1 = int(input())
odd_row_seats = int(input())
row_seats = 0
counter = 0

for s in range(ord("A"), ord(last_sector)+1):
    rows_sector1 += 1

    for r in range(1, rows_sector1):
        if r % 2 == 0:
            row_seats = odd_row_seats + 2
        elif r % 2 == 1:
            row_seats = odd_row_seats

        for p in range(1, row_seats+1):
            print(f"{chr(s)}{r}{chr(p+96)}")
            counter += 1

print(counter)
