from math import ceil
show_name = input()
show_time = int(input())
break_time = int(input())

lunch_time = break_time*0.125
rest_time = break_time*0.25
free_time_lunch_break_time = break_time-lunch_time-rest_time

deff = ceil(abs( show_time-free_time_lunch_break_time))

if show_time <= free_time_lunch_break_time:
    print(f"You have enough time to watch {show_name} and left with"
          f" {deff} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {deff} more minutes.")





