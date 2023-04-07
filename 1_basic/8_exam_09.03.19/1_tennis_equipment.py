from math import floor
from math import ceil

racket_price = float(input())
units_rackets = int(input())
units_shoes = int(input())

racket_total_price = units_rackets * racket_price
shoes_total_price = units_shoes * (racket_price / 6)
equipment = (shoes_total_price + racket_total_price) / 5

total_price = shoes_total_price + racket_total_price + equipment
octa_part = total_price / 8
print(f"Price to be paid by Djokovic {floor(octa_part)}")
print(f"Price to be paid by sponsors {ceil(octa_part * 7)}")
