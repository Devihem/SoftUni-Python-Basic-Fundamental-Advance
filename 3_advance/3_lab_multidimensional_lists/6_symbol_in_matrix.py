number_of_rows = int(input())

matrix = [[row for row in list(input())] for _ in range(number_of_rows)]
searched_element = input()

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == searched_element:
            print(f"({row}, {column})")
            quit()
else:
    print(f"{searched_element} does not occur in the matrix")
