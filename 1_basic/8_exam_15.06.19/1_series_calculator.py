from math import floor
tv_show_name = input()
seasons = int(input())
episodes = int(input())
length = float(input())

extra_ep_time = seasons * 10
ad_time = length * 0.2

total_time = (length + ad_time) * episodes * seasons + extra_ep_time

print(f"Total time needed to watch the {tv_show_name} series is {floor(total_time)} minutes.")
