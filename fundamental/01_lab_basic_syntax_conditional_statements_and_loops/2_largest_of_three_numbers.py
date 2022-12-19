number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

biggest_number = ""

if number_1 > number_2 and number_1 > number_3:
    biggest_number = number_1
elif number_2 > number_1 and number_2 > number_3:
    biggest_number = number_2
elif number_3 > number_1 and number_3 > number_2:
    biggest_number = number_3

print(biggest_number)
