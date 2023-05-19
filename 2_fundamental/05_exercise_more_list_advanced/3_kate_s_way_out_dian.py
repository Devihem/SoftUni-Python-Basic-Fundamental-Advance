def find_way_out(r, c, moves):
    if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
        return moves

    if matrix[r][c] == "#":
        return 0

    matrix[r][c] = "#"

    result1 = find_way_out(r + 1, c, moves + 1)
    result2 = find_way_out(r - 1, c, moves + 1)
    result3 = find_way_out(r, c + 1, moves + 1)
    result4 = find_way_out(r, c - 1, moves + 1)

    return max(result1, result2, result3, result4)


matrix = []
kate_pos = []

for row in range(int(input())):
    matrix.append(list(input()))

    if "k" in matrix[row]:
        kate_pos = [row, matrix[row].index("k")]

out_in = find_way_out(kate_pos[0], kate_pos[1], 0)

if not out_in:
    print(f"Kate cannot get out")
else:
    print(f"Kate got out in {out_in} moves")