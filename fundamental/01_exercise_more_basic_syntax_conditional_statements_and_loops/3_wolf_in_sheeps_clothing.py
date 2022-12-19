sheep_list = input()
sheep_order_list = sheep_list.split()
for order, animal in enumerate(reversed(sheep_order_list)):
    if order == 0 and "wolf" in animal:
        print("Please go away and stop eating my sheep")
    elif "wolf" in animal:
        print(f"Oi! Sheep number {order}! You are about to be eaten by a wolf!")