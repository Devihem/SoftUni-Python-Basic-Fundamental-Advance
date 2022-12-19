starting_year = int(input())
current_year = starting_year
flag = True
counter = 0
while flag:
    current_year += 1
    for digit in str(current_year):
        if str(current_year).count(digit) > 1:
            continue
        else:
            counter += 1
    if counter == len(str(current_year)):
        print(current_year)
        break
    else:
        counter = 0
