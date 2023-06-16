from collections import deque

caffeine = deque([int(x) for x in input().split(', ')])
drinks = deque([int(x) for x in input().split(', ')])
caffeine_count = 0
while caffeine and drinks:

    current_caffeine = caffeine.pop()
    current_drink = drinks.popleft()

    current_sum = current_caffeine * current_drink

    if caffeine_count + current_sum <= 300:
        caffeine_count += current_sum
        continue
    else:
        drinks.append(current_drink)
        caffeine_count -= 30
        if caffeine_count < 0:
            caffeine_count = 0

if drinks:
    print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_count} mg caffeine.")
# Final prints:
#  if all list are INTs : {', '.join([str(x) for x in list_name])}
