import Board
import copy
import random

board = Board.NQueens(10)
print("starting board")
board.print_board()

def agent(M, iterations):
    # Initialize the population with M random states
    population = [Board.NQueens(board.num_queens) for _ in range(M)]

    for i in range(iterations):
        # Evaluate the fitness of each state in the population
        population.sort(key=lambda x: x.fitness_function())
        best_state = population[0]
        best_fitness = best_state.fitness_function()

        print(f"Iteration: {i + 1} + Best Conflicts: {best_fitness}")

        if best_fitness == 0:
            print("Solution Found:")
            best_state.print_board()
            return

        # Generate all possible neighbors for the entire population
        all_neighbors = []
        for state in population:
            neighbors = []
            for _ in range(M):
                neighbor = state.get_neighbour()
                neighbor_board = copy.deepcopy(state)
                neighbor_board.set_state(neighbor)
                neighbors.append(neighbor_board)
            all_neighbors.extend(neighbors)

        # Sort all neighbors by fitness and select the top M to form the new population
        all_neighbors.sort(key=lambda x: x.fitness_function())
        population = all_neighbors[:M]

    print("Reached maximum iterations without finding a solution.")
    return None

# Run the local beam search with a population of size 5 and up to 1000 iterations
agent(5, 1000)
