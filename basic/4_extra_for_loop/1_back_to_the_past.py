money_heritage = float(input())
years_loop = int(input())

ivan_years = 18

for i in range(1800, years_loop+1):
    if i % 2 == 0:
        money_heritage = money_heritage - 12000
    elif i % 2 == 1:
        money_heritage = money_heritage - (12000 + 50 * ivan_years)
    ivan_years += 1

if money_heritage >= 0:
    print(f"Yes! He will live a carefree life and will have {money_heritage:.2f} dollars left.")
elif money_heritage < 0:
    print(f"He will need {-money_heritage:.2f} dollars to survive.")
