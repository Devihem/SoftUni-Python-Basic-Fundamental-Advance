place = input()
extra = input()
vip = input()
stays = int(input())
stay_price = 0
discount = 1
long_stay_bonus = 1

if stays < 1:
    print("Days must be positive number!")
    quit()
elif stays > 7:
    stays -= 1

if place not in ["Bansko", "Borovets", "Varna", "Burgas"] \
        or extra not in ["noEquipment",  "withEquipment", "noBreakfast", "withBreakfast"]:
    print("Invalid input!")
    quit()

elif place == "Bansko" or place == "Borovets":
    if extra == "noEquipment":
        stay_price = 80
        if vip == "yes":
            discount = 0.95
    elif extra == "withEquipment":
        stay_price = 100
        if vip == "yes":
            discount = 0.90

elif place == "Varna" or place == "Burgas":
    if extra == "noBreakfast":
        stay_price = 100
        if vip == "yes":
            discount = 0.93
    elif extra == "withBreakfast":
        stay_price = 130
        if vip == "yes":
            discount = 0.88

total_sum = stays * stay_price * discount
print(f"The price is {total_sum:.2f}lv! Have a nice time!")
