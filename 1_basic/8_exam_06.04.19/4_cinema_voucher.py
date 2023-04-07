voucher = int(input())
tickets = 0
others = 0
order = input()
while order != "End":
    if len(order) > 8:
        voucher -= ord(order[0]) + ord(order[1])
        if voucher < 0:
            break
        tickets += 1
    else:
        voucher -= ord(order[0])
        if voucher < 0:
            break
        others += 1
    order = input()

print(tickets)
print(others)
