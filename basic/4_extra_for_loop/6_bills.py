months_loop = int(input())

water_bills_fix = 20
internet_bills_fix = 15
electricity_bill_total = 0
other_bills_total = 0
water_bills_total = 0
internet_bills_total = 0

for i in range(0, months_loop):
    electricity_bills = float(input())
    electricity_bill_total += electricity_bills
    other_bills_total += (water_bills_fix + internet_bills_fix + electricity_bills) * 1.20
    water_bills_total += water_bills_fix
    internet_bills_total += internet_bills_fix

print(f"Electricity: {electricity_bill_total:.2f} lv")
print(f"Water: {water_bills_total:.2f} lv")
print(f"Internet: {internet_bills_total:.2f} lv")
print(f"Other: {other_bills_total:.2f} lv")
print(f"Average: {(water_bills_total + electricity_bill_total + internet_bills_total + other_bills_total)/months_loop:.2f} lv")

