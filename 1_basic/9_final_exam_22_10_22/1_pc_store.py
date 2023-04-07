processor_dol = float(input())
video_dol = float(input())
ram_dol = float(input())
ram_units = int(input())
discount = float(input())

dollar = 1.57

total_dol_sum = (ram_dol * ram_units) + ((processor_dol + video_dol) * (1 - discount))
total_sum_lev = total_dol_sum * dollar

print(f"Money needed - {total_sum_lev:.2f} leva.")
