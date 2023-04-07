miner_list = {}
while True:

    resource = input()
    if resource == "stop":
        break
    quantity = int(input())

    if resource not in miner_list:
        miner_list[resource] = quantity
    else:
        miner_list[resource] += quantity

[print(f"{key} -> {miner_list[key]}") for key in miner_list]
