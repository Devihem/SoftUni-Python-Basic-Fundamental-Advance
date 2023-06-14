def get_magic_triangle(rows):
    pyramid = []
    for counter in range(rows):
        current_row = [1 for _ in range(counter + 1)]
        pyramid.append(current_row)

    for row in range(1, len(pyramid)):
        for col in range(len(pyramid[row])):
            if 0 <= (col - 1) < len(pyramid[row - 1]):
                parent_1 = pyramid[row - 1][col - 1]
            else:
                parent_1 = 0

            if 0 <= col < len(pyramid[row - 1]):
                parent_2 = pyramid[row - 1][col]
            else:
                parent_2 = 0

            pyramid[row][col] = parent_1 + parent_2

    return pyramid


get_magic_triangle(5)