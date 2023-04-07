price_over_20kg = float(input())
baggage_kg = float(input())
day_to_travel = int(input())
bags_count = int(input())

price_under_10kg = price_over_20kg * 0.2
price_between_10kg_20kg = price_over_20kg * 0.5

baggage_price = 0
days_fee = 0

if baggage_kg < 10:
    baggage_price = price_under_10kg
elif 10 <= baggage_kg <= 20:
    baggage_price = price_between_10kg_20kg
else:
    baggage_price = price_over_20kg

if day_to_travel > 30:
    days_fee = 1.1
elif 7 <= day_to_travel <= 30:
    days_fee = 1.15
else:
    days_fee = 1.4

total_sum = baggage_price * days_fee * bags_count

print(f" The total price of bags is: {total_sum:.2f} lv. ")
