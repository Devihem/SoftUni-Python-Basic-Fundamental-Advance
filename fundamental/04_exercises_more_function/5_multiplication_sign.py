numbers_list = [int(input()), int(input()), int(input())]

negative_flag = False
zero_flag = False

for number_value in numbers_list:
    if number_value < 0:
        if negative_flag:
            negative_flag = False
        else:
            negative_flag = True
    elif number_value == 0:
        zero_flag = True

if zero_flag:
    print("zero")
elif negative_flag:
    print("negative")
else:
    print("positive")
