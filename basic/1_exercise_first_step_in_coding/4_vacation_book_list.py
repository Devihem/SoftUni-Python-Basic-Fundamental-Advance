total_pages = int(input())
pages_per_hour = int(input())
days = int(input())


per_day_reading_pages = total_pages/days
needed_time_per_day = per_day_reading_pages//pages_per_hour
print(needed_time_per_day)
