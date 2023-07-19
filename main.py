needed_money = float(input())
have = float(input())
days = 0
days_spending = 0

while have < needed_money:
    command = input()
    money = float(input())
    if command == 'save':
        have += money
        days += 1
        days_spending = 0

    elif command == 'spend':
        days += 1
        days_spending += 1
        if days_spending == 5:
            print(f"You can't save the money.")
            print(f"{days}")
            break

        if have < money:
            have = 0
        else:
            have -= money

if have >= needed_money:
    print(f"You saved the money for {days} days.")