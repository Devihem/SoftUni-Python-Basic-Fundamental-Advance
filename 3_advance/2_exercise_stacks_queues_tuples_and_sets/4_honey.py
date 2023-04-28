from collections import deque

bees = deque(int(x) for x in input().split())
nectar_list = deque(int(y) for y in input().split())
operators_list = deque(input().split())
total_honey = 0
while bees and nectar_list:
    current_bee = bees.popleft()
    current_nectar = nectar_list.pop()
    current_honey = 0
    if current_bee > current_nectar:
        bees.appendleft(current_bee)
        continue

    current_operator = operators_list.popleft()

    if current_operator == "+":
        current_honey = abs(current_bee + current_nectar)
    elif current_operator == "-":
        current_honey = abs(current_bee - current_nectar)
    elif current_operator == "*":
        current_honey = abs(current_bee * current_nectar)
    elif current_operator == "/":
        if current_nectar == 0:
            current_honey = abs(current_bee)
        else:
            current_honey = abs(current_bee / current_nectar)

    total_honey += current_honey

print(f"Total honey made: {total_honey}")
if bees:
    print("Bees left: ", end=''), print(*bees, sep=', ')
if nectar_list:
    print("Nectar left: ", end=''), print(*nectar_list, sep=', ')
