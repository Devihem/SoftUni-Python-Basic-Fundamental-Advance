from collections import deque

pizzas = deque([int(x) for x in input().split(', ')])
employees_cap = deque([int(x) for x in input().split(', ')])

total_pizzas_made = 0

while pizzas and employees_cap:

    current_pizza = pizzas.popleft()

    if current_pizza <= 0 or current_pizza > 10:
        continue

    current_employer = employees_cap.pop()

    if current_pizza <= current_employer:
        total_pizzas_made += current_pizza
        continue

    elif current_pizza > current_employer:
        pizzas.appendleft(current_pizza - current_employer)
        continue

if not pizzas:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas_made}')
    print(f'Employees: {", ".join([str(x) for x in employees_cap])}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizzas])}')
