import copy

board = []
max_count = 0
board_rows = int(input())
for row in range(board_rows):
    board.append(input().split(" "))

counter = 0
for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] == ".":
            # working board
            wb = copy.deepcopy(board)
            # starting seed = "+"
            wb[row][col] = "+"

            while True:
                counter = 0
                for m_row in range(len(wb)):
                    for m_col in range(len(wb[m_row])):
                        # if item is "." and  have "+" in 1 square around make it "+"
                        if wb[m_row][m_col] == ".":
                            # Check UP
                            if m_row != 0:
                                if wb[m_row - 1][m_col] == "+":
                                    wb[m_row][m_col] = "+"
                            # Check LEFT
                            if m_col != 0:
                                if wb[m_row][m_col - 1] == "+":
                                    wb[m_row][m_col] = "+"
                            # Check DOWN
                            if m_row != len(wb) - 1:
                                if wb[m_row + 1][m_col] == "+":
                                    wb[m_row][m_col] = "+"
                            # Check RIGHT
                            if m_col != len(wb[m_row]) - 1:
                                if wb[m_row][m_col + 1] == "+":
                                    wb[m_row][m_col] = "+"
                            # Added Counter + 1
                            if wb[m_row][m_col] == "+":
                                counter += 1

                if counter == 0:
                    current_max = 0
                    for count_row in wb:
                        for symbol in count_row:
                            if symbol == "+":
                                current_max += 1
                    if max_count < current_max:
                        max_count = current_max
                    break

print(max_count)
