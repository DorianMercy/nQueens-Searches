import Board
import random
import copy

class GeneticAlgorithmNQueens:
    def __init__(self, num_queens, population_size, mutation_rate, patience=50):
        self.num_queens = num_queens
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.patience = patience  # Number of generations to wait for improvement

    def initialize_population(self):
        return [Board.NQueens(self.num_queens) for _ in range(self.population_size)]

    def fitness(self, state):
        return state.fitness_function()

    def select_parents(self, population):
        """Roulette Wheel Selection"""
        fitnesses = [1 / (self.fitness(state) + 1) for state in population]  # Inverted fitness for selection
        total_fitness = sum(fitnesses)
        selection_probs = [fitness / total_fitness for fitness in fitnesses]
        parent1 = random.choices(population, weights=selection_probs, k=1)[0]
        parent2 = random.choices(population, weights=selection_probs, k=1)[0]
        return parent1, parent2

    def crossover(self, parent1, parent2):
        """Single-point crossover"""
        crossover_point = random.randint(0, self.num_queens - 1)
        child_state = parent1.state[:crossover_point] + parent2.state[crossover_point:]
        child = Board.NQueens(self.num_queens)
        child.set_state(child_state)
        return child

    def mutate(self, individual):
        """Randomly mutate a single gene"""
        if random.random() < self.mutation_rate:
            col = random.randint(0, self.num_queens - 1)
            row = random.randint(0, self.num_queens - 1)
            individual.state[col] = row

    def run(self, max_generations):
        population = self.initialize_population()
        best_fitness = float('inf')
        best_individual = None
        no_improvement_generations = 0

        for generation in range(max_generations):
            population.sort(key=lambda x: self.fitness(x))
            current_best_individual = population[0]
            current_best_fitness = self.fitness(current_best_individual)

            print(f"Generation {generation + 1}: Best Fitness = {current_best_fitness}")

            if current_best_fitness == 0:
                print("Solution Found:")
                current_best_individual.print_board()
                return current_best_individual

            if current_best_fitness < best_fitness:
                best_fitness = current_best_fitness
                best_individual = copy.deepcopy(current_best_individual)
                no_improvement_generations = 0
            else:
                no_improvement_generations += 1

            # Check if stuck in local optima
            if no_improvement_generations >= self.patience:
                print(f"Stuck in local optima after {generation + 1} generations.")
                print("Best solution found so far:")
                best_individual.print_board()
                return best_individual

            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = self.select_parents(population)
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                new_population.append(child)

            population = new_population

        print("Reached maximum generations without finding a solution.")
        return None

# Example Usage:
genetic_solver = GeneticAlgorithmNQueens(num_queens=10, population_size=100, mutation_rate=0.1)
genetic_solver.run(max_generations=1000)
