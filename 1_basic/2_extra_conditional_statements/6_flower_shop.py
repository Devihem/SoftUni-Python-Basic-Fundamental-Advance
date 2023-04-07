from math import    ceil, floor
magnolias = 3.25
hyacinths = 4
roses = 3.5
cacti = 8

magnolias_pieces = int(input())
hyacinths_pieces = int(input())
roses_pieces = int(input())
cacti_pieces = int(input())
gift_price = float(input())

total_sum = (magnolias*magnolias_pieces + hyacinths_pieces*hyacinths + roses_pieces*roses + cacti_pieces*cacti)*0.95

deff = abs (total_sum - gift_price)


if (total_sum - gift_price) >= 0:
    print(f"She is left with {floor(deff)} leva.")
elif (gift_price - total_sum) >= 0:
    print(f"She will have to borrow {ceil(deff)} leva.")
