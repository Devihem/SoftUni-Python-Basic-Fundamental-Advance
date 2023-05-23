def math_operations(*args, **kwargs):
    numbers = list(args)
    counter = 0
    while True:
        counter += 1
        if numbers:
            new_number = numbers.pop(0)
        else:
            break

        if counter == 1:
            kwargs['a'] += new_number

        elif counter == 2:
            kwargs['s'] -= new_number

        elif counter == 3:
            if new_number > 0:
                kwargs['d'] /= new_number

        elif counter == 4:
            kwargs['m'] *= new_number

        if not numbers:
            break
        if counter == 4:
            counter = 0
    return '\n'.join([f'{key}: {value:.1f}' for key, value in sorted(kwargs.items(), key=lambda k: (-k[1], k[0]))])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
