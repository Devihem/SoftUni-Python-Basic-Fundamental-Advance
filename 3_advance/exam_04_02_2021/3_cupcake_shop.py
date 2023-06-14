# sloppy solved

from collections import deque


def stock_availability(inventory_list, delivery_or_sell, *extra_param_str_int):
    inventory_deque = deque(inventory_list)
    if delivery_or_sell == 'delivery':
        inventory_deque.extend(extra_param_str_int)
    elif delivery_or_sell == 'sell':
        if not extra_param_str_int:
            inventory_deque.popleft()
        elif str(extra_param_str_int[0]).isdigit():
            for count in range(extra_param_str_int[0]):
                inventory_deque.popleft()
        else:
            for flavor in extra_param_str_int:
                while flavor in inventory_deque:
                    inventory_deque.remove(flavor)

    return list(inventory_deque)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
