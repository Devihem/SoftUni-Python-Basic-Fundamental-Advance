from collections import deque

quantity_food = int(input())
each_order_quantity = deque([int(x) for x in input().split(' ')])
print(max(each_order_quantity))

while len(each_order_quantity) > 0:
    if quantity_food < each_order_quantity[0]:
        print(f"Orders left: ", end='')
        print(*each_order_quantity, sep=' ')
        break

    served_quantity = each_order_quantity.popleft()
    quantity_food -= served_quantity
else:
    print("Orders complete")
