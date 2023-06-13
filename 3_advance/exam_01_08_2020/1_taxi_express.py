from collections import deque

customers_list = deque(int(x) for x in input().split(', '))
taxi_list = deque(int(x) for x in input().split(', '))
total_time = 0

while customers_list and taxi_list:
    current_customer = customers_list.popleft()
    current_taxi = taxi_list.pop()
    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers_list.appendleft(current_customer)

if not customers_list:
    print("All customers were driven to their destinations"
          f"\nTotal time: {total_time} minutes")
elif not taxi_list:
    print("Not all customers were driven to their destinations"
          f"\nCustomers left: {', '.join([str(x) for x in customers_list])}")
