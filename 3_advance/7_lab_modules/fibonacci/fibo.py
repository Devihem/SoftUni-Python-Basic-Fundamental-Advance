def create_seq(count):
    if count == 1:
        return [0]

    if count == 2:
        return [0, 1]

    fib_list = [0, 1]
    for num in range(2, count):
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)

    return fib_list


def locate_num(num, seq):
    try:
        index = seq.index(num)
        return f'The number - {num} is at index {index}'
    except ValueError:
        return f"The number {num} is not in the sequence"
