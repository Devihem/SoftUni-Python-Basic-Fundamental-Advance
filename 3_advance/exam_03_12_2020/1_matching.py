from collections import deque

males_int_list = deque([int(numb) for numb in input().split()])
females_int_list = deque([int(numb) for numb in input().split()])
match_list = []

while males_int_list and females_int_list:

    current_m = males_int_list.pop()

    current_f = females_int_list.popleft()

    if current_m < 1:
        females_int_list.appendleft(current_f)
        continue
    if current_f < 1:
        males_int_list.append(current_m)
        continue

    if current_m % 25 == 0 and current_f % 25 == 0:
        current_m = males_int_list.pop()
        current_f = females_int_list.popleft()
        continue

    if current_m % 25 == 0:
        current_m = males_int_list.pop()
        females_int_list.appendleft(current_f)
        continue

    if current_f % 25 == 0:
        current_f = females_int_list.popleft()
        males_int_list.append(current_m)
        continue

    if current_m == current_f:
        match_list.append(current_m)
    else:
        current_m = current_m - 2
        males_int_list.append(current_m)

print(f"Matches: {len(match_list)}")
if males_int_list:
    print(f"Males left: {', '.join([str(x) for x in list(reversed(males_int_list))])}")
else:
    print("Males left: none")

if females_int_list:
    print(f"Females left: {', '.join([str(x) for x in females_int_list])}")
else:
    print("Females left: none")
