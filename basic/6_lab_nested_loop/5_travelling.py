end_travel_flag = False
total_saved_money = 0

while not end_travel_flag:
    travel_place = input()
    if travel_place == "End":
        end_travel_flag = True
        break
    else:
        travel_price = float(input())
        new_destination_flag = True
        while new_destination_flag:
            saved_money = float(input())
            total_saved_money += saved_money
            if total_saved_money >= travel_price:
                print(f"Going to {travel_place}!")
                total_saved_money = 0
                new_destination_flag = False
