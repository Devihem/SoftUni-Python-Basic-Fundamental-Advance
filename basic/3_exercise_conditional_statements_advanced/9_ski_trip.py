day_staying = int(input())
place_type = input()
rating = input()

booking_price = 0
room_bonus = 1
apartment_bonus = 1
pr_apartment = 1
end_sum = 0

if day_staying < 10:
    apartment_bonus = 0.7
    pr_apartment = 0.9
elif 10 <= day_staying <= 15:
    apartment_bonus = 0.65
    pr_apartment = 0.85
elif day_staying > 15:
    apartment_bonus = 0.5
    pr_apartment = 0.8

if place_type == "room for one person":
    booking_price = 18 * (day_staying - 1)
elif place_type == "apartment":
    booking_price = 25 * (day_staying - 1) * apartment_bonus
elif place_type == "president apartment":
    booking_price = 35 * (day_staying - 1) * pr_apartment

if rating == "negative":
    end_sum = booking_price * 0.9
elif rating == "positive":
    end_sum = booking_price * 1.25

print(f"{end_sum:.2f}")
