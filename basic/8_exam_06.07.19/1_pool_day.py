from math import ceil
people = int(input())
entry_fee = float(input())
lounge = float(input())
umbrella = float(input())

entre_fee_tax = people * entry_fee
umbrella_tax = ceil(people/2) * umbrella
lounge_tax = ceil(people*0.75) * lounge

total_sum = lounge_tax + umbrella_tax + entre_fee_tax
print(f"{total_sum:.2f} lv.")
