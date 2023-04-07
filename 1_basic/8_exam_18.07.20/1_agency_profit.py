airplane_co_name = input()
adult_tickets = int(input())
children_tickets = int(input())
adult_ticket_price = float(input())
tax = float(input())

children_ticket_price = adult_ticket_price * 0.3

total_adult_income = adult_tickets * (adult_ticket_price + tax)
total_children_income = children_tickets * (children_ticket_price + tax)

total_sum = total_adult_income + total_children_income
air_company_income = total_sum * 0.2

print(f"The profit of your agency from {airplane_co_name} tickets is {air_company_income:.2f} lv.")
