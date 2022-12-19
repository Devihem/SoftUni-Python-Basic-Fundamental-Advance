size = float(input())
price = 7.61
total_sum = size*price
discount = total_sum*0.18
final_payment = total_sum - discount

print(f"The final price is: {final_payment} lv.")
print(f"The discount is: {discount} lv.")
