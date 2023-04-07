year_tax = int(input())

snickers = year_tax * 0.60
clothes = snickers * 0.80
b_ball = clothes * 0.25
accessories = b_ball * 0.20

total = year_tax + snickers + clothes +b_ball + accessories

print(f"{total:.2f}")