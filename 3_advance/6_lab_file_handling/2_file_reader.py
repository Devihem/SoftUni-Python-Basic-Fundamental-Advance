with open('numbers.txt') as file:
    sum_file_nums = 0
    for line in file.readlines():
        sum_file_nums += int(line)
    print(sum_file_nums)
