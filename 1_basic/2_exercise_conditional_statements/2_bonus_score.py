number_input = int(input())
bonus = 0

if number_input <= 100:
    bonus = 5
elif number_input <= 1000:
    bonus = number_input*0.20
else:
    bonus = number_input*0.10

if number_input % 2 == 0:
    bonus = bonus+1
elif number_input % 10 == 5:
    bonus = bonus+2

print(bonus)
print(number_input+bonus)
