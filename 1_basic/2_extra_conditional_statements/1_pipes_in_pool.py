V_volume_pool_l = int(input())
P1_flow_rate_h = int(input())
P2_flow_rate_h = int(input())
H_missing_hours = float(input())

P_total_flow_rate = P1_flow_rate_h+P2_flow_rate_h
water_in_pool = H_missing_hours * P_total_flow_rate
overflow_rate= abs(water_in_pool-V_volume_pool_l)

water_in_pool_percent = water_in_pool/(V_volume_pool_l/100)

P1_flow_rate_percent = P1_flow_rate_h/(P_total_flow_rate/100)
P2_flow_rate_percent = P2_flow_rate_h/(P_total_flow_rate/100)

if water_in_pool > V_volume_pool_l:
    print(f"For {H_missing_hours} hours the pool overflows with {overflow_rate:.2f} liters.")
else:
    print(f"The pool is {water_in_pool_percent:.2f}% full."
          f" Pipe 1: {P1_flow_rate_percent:.2f}%. Pipe 2: {P2_flow_rate_percent:.2f}%.")

