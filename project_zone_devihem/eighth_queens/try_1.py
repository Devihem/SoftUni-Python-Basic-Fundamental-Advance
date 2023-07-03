def place_queen(matrix):
    free = ' '
    for row in range(b_size):
        for col in range(b_size):
            if b_matrix[row][col] == free:
                b_matrix[row][col] = 'Q'
    else:
        return matrix


b_size = 8
b_matrix = [[' ' for x in range(b_size)] for _ in range(b_size)]
print(*b_matrix, sep="\n")

b_matrix = place_queen(b_matrix)




print()
print(*b_matrix, sep="\n")