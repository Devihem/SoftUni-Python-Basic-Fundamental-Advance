lili_years = int(input())
washing_machine = float(input())
toys_value = int(input())

money = 0
toys_money = 0

for i in range(1, lili_years+1):
    if i % 2 == 0:
        money = money + ((i/2)*10) - 1
    elif i % 2 == 1:
        toys_money += toys_value

total = money + toys_money
diff = abs(washing_machine-total)
if washing_machine <= total:
    print(f"Yes! {diff:.2f}")

elif total < washing_machine:
    print(f"No! {diff:.2f}")
