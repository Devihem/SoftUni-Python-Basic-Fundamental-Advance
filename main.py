degrees = int(input())
time_of_the_day = input()

time_of_the_day_possibilities_tuple = ("Morning", "Afternoon", "Evening")
outfit_list = ["Sweatshirt", "Shirt", "T-Shirt", "Swim Suit"]
shoes_list = ["Sneakers", "Moccasins", "Sandals", "Barefoot"]

if 10 <= degrees <= 18 and time_of_the_day == time_of_the_day_possibilities_tuple[0]:
    print(f"It's {degrees} degrees, get your {outfit_list[0]} and {shoes_list[0]}.")

elif 10 <= degrees <= 18 and time_of_the_day == time_of_the_day_possibilities_tuple[1]:
    print(f"It's {degrees} degrees, get your {outfit_list[1]} and {shoes_list[1]}.")

elif 10 <= degrees <= 18 and time_of_the_day == time_of_the_day_possibilities_tuple[2]:
    print(f"It's {degrees} degrees, get your {outfit_list[1]} and {shoes_list[1]}.")

elif 18 < degrees <= 24 and time_of_the_day == time_of_the_day_possibilities_tuple[0]:
    print(f"It's {degrees} degrees, get your {outfit_list[1]} and {shoes_list[1]}.")

elif 18 < degrees <= 24 and time_of_the_day == time_of_the_day_possibilities_tuple[1]:
    print(f"It's {degrees} degrees, get your {outfit_list[2]} and {shoes_list[2]}.")

elif 18 < degrees <= 24 and time_of_the_day == time_of_the_day_possibilities_tuple[2]:
    print(f"It's {degrees} degrees, get your {outfit_list[1]} and {shoes_list[1]}.")

elif degrees >= 25 and time_of_the_day == time_of_the_day_possibilities_tuple[0]:
    print(f"It's {degrees} degrees, get your {(outfit_list[2])} and {(shoes_list[2])}.")

elif degrees >= 25 and time_of_the_day == time_of_the_day_possibilities_tuple[1]:
    print(f"It's {degrees} degrees, get your {(outfit_list[3])} and {(shoes_list[3])}.")

elif degrees >= 25 and time_of_the_day == time_of_the_day_possibilities_tuple[2]:
    print(f"It's {degrees} degrees, get your {(outfit_list[1])} and {(shoes_list[1])}.")
