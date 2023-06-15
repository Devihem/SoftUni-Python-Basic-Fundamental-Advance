from collections import deque

ramens = deque([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])

while ramens and customers:

    ramen = ramens.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue

    elif ramen > customer:
        ramen -= customer
        ramens.append(ramen)

    elif ramen < customer:
        customer -= ramen
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if ramens:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in ramens])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")