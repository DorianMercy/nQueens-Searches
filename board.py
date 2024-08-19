import random


class NQueens:
    def __init__(self, num_queens):
        self.num_queens = num_queens
        self.state = [random.randint(0, num_queens - 1) for _ in range(num_queens)]

    def print_board(self):
        board = [['.' for _ in range(self.num_queens)] for _ in range(self.num_queens)]
        for col, row in enumerate(self.state):
            board[row][col] = 'Q'
        for row in board:
            print(' '.join(row))
        print("\n")

    def fitness_function(self):
        conflicts = 0
        for i in range(self.num_queens):
            for j in range(i + 1, self.num_queens):
                if self.state[i] == self.state[j]:
                    conflicts += 1
                if abs(self.state[i] - self.state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def get_neighbour(self):
        """Only gets a single neighbour"""
        neighbour = self.state[:]
        col = random.randint(0, self.num_queens - 1)
        row = random.randint(0, self.num_queens - 1)
        neighbour[col] = row
        return neighbour

    def set_state(self, new_state):
        self.state = new_state
