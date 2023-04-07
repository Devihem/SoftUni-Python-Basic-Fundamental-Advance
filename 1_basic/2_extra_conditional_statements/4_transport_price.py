travel_length_km= int(input())
time_diapason = input()

taxi_start_tax = 0.7
taxi_day = 0.79
taxi_night = 0.90
bus_day_night = 0.09
train_day_night = 0.06
taxi_price = 0

if time_diapason == "day":
    taxi_price = taxi_start_tax+travel_length_km*taxi_day
elif time_diapason == "night":
    taxi_price = taxi_start_tax+travel_length_km*taxi_night

bus_price = travel_length_km*bus_day_night
train_price = travel_length_km*train_day_night


if travel_length_km < 20:
    best_value = taxi_price
elif travel_length_km < 100:
    best_value = min(taxi_price,bus_price)
else:
    best_value = min(taxi_price,bus_price,train_price)

print(f"{best_value:.2f}")
