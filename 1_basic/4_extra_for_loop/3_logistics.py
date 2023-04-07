cargo_loop = int(input())

bus_tons = 0
truck_tons = 0
train_tons = 0

bus_transit = 0
train_transit = 0
truck_transit = 0

for i in range(0, cargo_loop):
    weight = int(input())
    if weight <= 3:
        bus_tons += weight
        bus_transit += 1
    elif 4 <= weight <= 11:
        truck_tons += weight
        truck_transit += 1
    elif weight >= 12:
        train_tons += weight
        train_transit += 1

total_tons = bus_tons + truck_tons + train_tons
total_price = 200 * bus_tons + 175 * truck_tons + 120 * train_tons

print(f"{total_price/total_tons:.2f}")
print(f"{(bus_tons/total_tons)*100:.2f}%")
print(f"{(truck_tons/total_tons)*100:.2f}%")
print(f"{(train_tons/total_tons)*100:.2f}%")
