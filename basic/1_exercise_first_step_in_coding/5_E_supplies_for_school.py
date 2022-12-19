markers_box_needed = int(input())
pens_box_needed = int(input())
cleaning_stuff_needed = int(input())
today_discount = int(input())

markers_box = 5.80
pens_box = 7.20
cleaning_stuff_per_liter = 1.20

total = (markers_box*markers_box_needed + pens_box*pens_box_needed +
         cleaning_stuff_per_liter*cleaning_stuff_needed) * (1-(today_discount/100))

print(total)