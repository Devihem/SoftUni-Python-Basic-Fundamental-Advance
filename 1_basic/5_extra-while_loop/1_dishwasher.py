detergent_bottles = int(input())
detergent_ml = detergent_bottles * 750
dishwasher_counter = 0

pans_count = 0
dish_count = 0

while detergent_ml >= 0:
    working_task = input()
    dishwasher_counter += 1
    if working_task == "End":
        break
    else:
        working_task = int(working_task)

    if dishwasher_counter % 3 == 0:
        detergent_ml = detergent_ml - working_task * 15
        pans_count = pans_count + working_task
    else:
        detergent_ml = detergent_ml - working_task * 5
        dish_count = dish_count + working_task

if detergent_ml >= 0:
    print("Detergent was enough!")
    print(f"{dish_count} dishes and {pans_count} pots were washed.")
    print(f"Leftover detergent {detergent_ml} ml.")
elif detergent_ml < 0:
    print(f"Not enough detergent, {-detergent_ml} ml. more necessary!")
