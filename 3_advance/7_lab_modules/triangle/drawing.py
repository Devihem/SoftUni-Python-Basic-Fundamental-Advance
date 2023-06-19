def draw_upper_part(n):
    for row in range(1, n + 1):
        for num in range(1, row + 1):
            print(num, end=' ')
        print()


def draw_bottom_part(n):
    for row in range(n-1, 0, -1):
        for num in range(1, row + 1):
            print(num, end=' ')
        print()


def draw_numbers_triangle(n):
    draw_upper_part(n)
    draw_bottom_part(n)


