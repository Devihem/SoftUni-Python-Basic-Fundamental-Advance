money_distribution = [int(number) for number in input().split(", ")]
equilibrium_value = int(input())

if sum(money_distribution) / len(money_distribution) < equilibrium_value:
    print("No equal distribution possible")
else:
    while min(money_distribution) != equilibrium_value:
        max_value = max(money_distribution)
        max_value_index = money_distribution.index(max_value)
        min_value = min(money_distribution)
        min_value_index = money_distribution.index(min_value)
        money_distribution[max_value_index] -= equilibrium_value - min_value
        money_distribution[min_value_index] += equilibrium_value - min_value
    print(money_distribution)
