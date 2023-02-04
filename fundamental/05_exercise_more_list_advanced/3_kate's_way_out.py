def starting_values_and_map_5_3():
    rows_in_maze = int(input())
    map_rc = [list(input()) for _ in range(rows_in_maze)]
    return map_rc


# r_c = rows and columns
r_c = starting_values_and_map_5_3()
print(r_c)
print(r_c[1][4])
