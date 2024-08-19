import board
import copy

"""Look at population approach and simulated annealing"""
"""Alter number of queens and columns using constructor"""
board = board.NQueens(10)
print("starting board")
board.print_board()


def agent(iterations):
    for i in range(iterations):
        goal_test = board.fitness_function()
        print(f"Iteration: {i + 1} + Conflicts: {goal_test}")
        if goal_test == 0:
            print("Solution Found:")
            board.print_board()
            return
        """Generate Neighbours"""
        for j in range(iterations):
            neighbour = board.get_neighbour()
            neighbour_board = copy.deepcopy(board)
            neighbour_board.set_state(neighbour)
            """First Choice Hill Climbing: Takes first state that is better"""
            if neighbour_board.fitness_function() < board.fitness_function(): # Why set a limit to side-steps?
                board.set_state(neighbour)
                break
            """Stopping Criteria"""
            if j + 1 == iterations:
                print("Stuck in Local Optima")
                return None


agent(1000)


