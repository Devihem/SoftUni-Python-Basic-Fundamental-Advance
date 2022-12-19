chrysanthemums_order = int(input())
roses_order = int(input())
tulips_order = int(input())
season = input()
special_day = input()
extra_price = 1
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0


if season == "Summer" or season == "Spring":
    chrysanthemums_price = 2
    roses_price = 4.10
    tulips_price = 2.5
elif season == "Winter" or season == "Autumn":
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

if special_day == "Y":
    extra_price = 1.15

bouquet_price = (roses_order * roses_price + chrysanthemums_price*chrysanthemums_order + tulips_order * tulips_price)\
                * extra_price

if tulips_order > 7 and season == "Spring":
    bouquet_price = bouquet_price * 0.95

if roses_order >= 10 and season == "Winter":
    bouquet_price = bouquet_price * 0.90

if roses_order + tulips_order + chrysanthemums_order > 20:
    bouquet_price = bouquet_price * 0.80

end_price = bouquet_price +2

print(f"{end_price:.2f}")

