total_sum = 0
while True:
    money = input()
    if money == "NoMoreMoney":
        break
    money = float(money)
    if money < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {money:.2f}")
        total_sum += money

print(f"Total: {total_sum:.2f}")
