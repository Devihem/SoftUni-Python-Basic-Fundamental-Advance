deposit = int(input())
deposit_time = int(input())
deposit_procent = float(input())
money_total_procent = deposit*(deposit_procent/100)
deposit_per_mount = money_total_procent/12
total_sum = deposit+deposit_per_mount*deposit_time
print(total_sum)
