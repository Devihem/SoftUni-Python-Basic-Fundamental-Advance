coin_1_lev = int(input())
coin_2_lev = int(input())
coin_5_lev = int(input())
total_sum = int(input())

for x3 in range(0, coin_1_lev+1):
    for x2 in range(0, coin_2_lev+1):
        for x1 in range(0, coin_5_lev+1):
            if x1*5+x2*2+x3*1 == total_sum:
                print(f"{x3} * 1 lv. + {x2} * 2 lv. + {x1} * 5 lv. = {total_sum} lv.")