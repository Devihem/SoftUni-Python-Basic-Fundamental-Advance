from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milks = deque(int(y) for y in input().split(', '))
milkshakes = 0

while milkshakes < 5 and milks and chocolates:

    current_milk = milks.popleft()
    current_chocolate = chocolates.pop()
    if current_milk <= 0 and current_chocolate <= 0:
        continue
    elif current_chocolate <= 0:
        milks.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk > 0:
        milkshakes += 1
    else:
        milks.append(current_milk)
        chocolates.append(current_chocolate + (- 5))

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: ", end=''), print(*chocolates, sep=', ')
else:
    print("Chocolate: empty")

if milks:
    print(f"Milk: ", end=''), print(*milks, sep=', ')
else:
    print("Milk: empty")
