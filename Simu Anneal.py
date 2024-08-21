import math
import random
import copy
import board  # Import your NQueens class

def agent(iterations, initial_temperature, cooling_rate):
    current_board = board
    temperature = initial_temperature

    for i in range(iterations):
        goal_test = current_board.fitness_function()
        print(f"Iteration: {i + 1} + Conflicts: {goal_test}")
        
        if goal_test == 0:
            print("Solution Found:")
            current_board.print_board()
            return
        
        # Generate Neighbour
        neighbour = current_board.get_neighbour()
        neighbour_board = copy.deepcopy(current_board)
        neighbour_board.set_state(neighbour)
        
        current_fitness = current_board.fitness_function()
        neighbour_fitness = neighbour_board.fitness_function()
        
        delta_e = neighbour_fitness - current_fitness
        
        if neighbour_fitness < current_fitness:
            # Accept the neighbour if it's better
            current_board.set_state(neighbour)
        else:
            # Accept the neighbour with a probability based on temperature
            acceptance_probability = math.exp(-delta_e / temperature)
            if random.random() < acceptance_probability:
                current_board.set_state(neighbour)
        
        # Update temperature
        temperature *= cooling_rate
        
        # Stopping criteria
        if temperature < 1e-5:  # A small threshold to terminate the process
            print("Temperature too low, stopping...")
            break

    print("Terminating...")
    current_board.print_board()

# Initialize board
board = board.NQueens(10)
print("Starting board")
board.print_board()

# Run the agent with simulated annealing
agent(iterations=1000, initial_temperature=1000, cooling_rate=0.99)
