clients_number_loop = int(input())

basket = 1.50
wreath = 3.80
chocolate_bunny = 7
items_counter = 0
client_total_sum = 0
price = 0
total_shop_income = 0

for i in range(0, clients_number_loop):
    while True:
        command = input()
        if command == "Finish":
            if items_counter % 2 == 0:
                client_total_sum = client_total_sum * 0.8
            print(f"You purchased {items_counter} items for {client_total_sum:.2f} leva.")
            break
        elif command == "basket":
            price = basket
            items_counter += 1
        elif command == "wreath":
            price = wreath
            items_counter += 1
        elif command == "chocolate bunny":
            price = chocolate_bunny
            items_counter += 1

        client_total_sum += price
    total_shop_income += client_total_sum
    client_total_sum = 0
    items_counter = 0

print(f"Average bill per client is: {total_shop_income / clients_number_loop :.2f} leva.")
