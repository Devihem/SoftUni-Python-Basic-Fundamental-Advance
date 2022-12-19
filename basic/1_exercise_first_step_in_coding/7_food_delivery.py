o_chicken = int(input())
o_fish = int(input())
o_vegetables = int(input())

chicken = 10.35
fish = 12.40
vegetables = 8.15
delivery = 2.5

order_price = chicken*o_chicken+fish*o_fish+vegetables*o_vegetables
desert = 0.20*order_price

total = order_price+desert+delivery
print(f"{total:.2f}")


