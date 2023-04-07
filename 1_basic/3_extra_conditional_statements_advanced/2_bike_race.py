junior_group = int(input())
senior_group = int(input())
race_type = input()

junior_entry = 0
senior_entry = 0

if race_type == "trail":
    junior_entry = 5.50
    senior_entry = 7
elif race_type == "cross-country":
    junior_entry = 8
    senior_entry = 9.50
    if senior_group + junior_group >= 50:
        junior_entry = 8 * 0.75
        senior_entry = 9.50 * 0.75
elif race_type == "downhill":
    junior_entry = 12.25
    senior_entry = 13.75
elif race_type == "road":
    junior_entry = 20
    senior_entry = 21.50

total_sum_for_donation = (junior_entry * junior_group + senior_entry * senior_group) * 0.95

print(f"{total_sum_for_donation:.2f}")
