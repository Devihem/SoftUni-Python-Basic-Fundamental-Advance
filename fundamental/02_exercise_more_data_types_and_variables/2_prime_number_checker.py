number_loop = int(input())

for number in range(2, number_loop):
    if number_loop % number == 0:
        print("False")
        break
else:
    print("True")
