record_time_sec = float(input())
length = float(input())
m_per_sec = float(input())

swiming_time_sec_clear = length * m_per_sec
water_resistant_adding_time = (length//15) * 12.5


total_swiming_time = swiming_time_sec_clear+water_resistant_adding_time

deff = abs(record_time_sec-total_swiming_time)

if total_swiming_time < record_time_sec:
    print(f"Yes, he succeeded! The new world record is {total_swiming_time:.2f} seconds.")

elif total_swiming_time >= record_time_sec:
    print(f"No, he failed! He was {deff:.2f} seconds slower.")
