snowballs_count = int(input())
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_value = 0
best_snowball_quality = 0
last_snowball_value = 0
for snowball in range(snowballs_count):
    snowball_weight = int(input())
    snowball_time_needed = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time_needed) ** snowball_quality
    if snowball_value > last_snowball_value:
        last_snowball_value = snowball_value
        best_snowball_weight = snowball_weight
        best_snowball_time = snowball_time_needed
        best_snowball_value = int(snowball_value)
        best_snowball_quality = snowball_quality


print(f"{best_snowball_weight} : {best_snowball_time} = {best_snowball_value} ({best_snowball_quality})")