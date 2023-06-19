from fibonacci.fibo import create_seq, locate_num

seq = []

while True:
    data = input()

    if data == 'Stop':
        break

    split_data = data.split()

    if split_data[0] == 'Create':
        n = int(split_data[-1])
        seq = create_seq(n)
        print(*seq)
    elif split_data[0] == 'Locate':
        num = int(split_data[-1])
        print(locate_num(num, seq))
