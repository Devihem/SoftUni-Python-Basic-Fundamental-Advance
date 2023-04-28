import heapq


class Puzzle:
    def __init__(self, board, g=0, h=0):
        self.board = board
        self.g = g
        self.h = h

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        return self.board == other.board

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.board])

    def find_blank(self):
        for i, row in enumerate(self.board):
            if '□' in row:
                j = row.index('□')
                return i, j

    def move(self, di, dj):
        i, j = self.find_blank()
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            new_board = [list(row) for row in self.board]
            new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
            return Puzzle(new_board, self.g + 1, self.manhattan_distance())

    def expand(self):
        return [self.move(di, dj) for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]]

    def is_solved(self):
        return str(self) == ' 1  2  3  4\n 5  6  7  8\n 9 10 11 12\n13 14 15 □'

    def manhattan_distance(self):
        distance = 0
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                if tile != '□':
                    tile_num = int(tile)
                    goal_i, goal_j = (tile_num - 1) // 4, (tile_num - 1) % 4
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance


def solve(puzzle):
    start = Puzzle(puzzle)
    heap = [start]
    visited = set()
    while heap:
        puzzle = heapq.heappop(heap)
        if puzzle.is_solved():
            return puzzle.g, puzzle
        visited.add(puzzle)
        for next_puzzle in puzzle.expand():
            if next_puzzle not in visited:
                heapq.heappush(heap, next_puzzle)
    return -1, None


puzzle_grid = [[' □', ' 2', ' 3', ' 4'], [' 5', ' 6', ' 7', ' 8'], [' 9', '10', '11', '12'], ['13', '14', '15', ' 1']]

moves, solution = solve(puzzle_grid)

if solution is not None:wheel
    print(f"Solved in {moves} moves:\n{solution}")
else:
    print("Unable to solve puzzle.")
