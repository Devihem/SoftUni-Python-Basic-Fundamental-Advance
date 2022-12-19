wanted_income = float(input())
current_income = 0

while current_income < wanted_income:
    cocktail = input()
    if cocktail == "Party!":
        break
    cocktail_count = int(input())
    cocktail_price = len(cocktail)
    current_bill = cocktail_price * cocktail_count

    if int(repr(current_bill)[-1]) % 2 != 0:
        current_bill *= 0.75

    current_income += current_bill
    current_bill = 0

if current_income < wanted_income:
    print(f"We need {wanted_income - current_income :.2f} leva more.")
else:
    print("Target acquired.")
print(f"Club income - {current_income:.2f} leva.")