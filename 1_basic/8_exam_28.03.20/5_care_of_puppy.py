food_bought = int(input())
total_food = food_bought * 1000
while True:
    status = input()
    if status == "Adopted":
        if total_food >= 0:
            print(f"Food is enough! Leftovers: {total_food} grams.")
            break
        elif total_food < 0:
            print(f"Food is not enough. You need {-total_food} grams more.")
            break
    else:
        status = int(status)
    total_food -= status
