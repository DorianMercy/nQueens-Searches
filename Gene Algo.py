import random

class GeneticAlgorithmNQueens:
    def __init__(self, num_queens, population_size, mutation_rate, max_generations):
        self.num_queens = num_queens
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.population = [self.random_individual() for _ in range(population_size)]

    def random_individual(self):
        return [random.randint(0, self.num_queens - 1) for _ in range(self.num_queens)]

    def fitness(self, individual):
        conflicts = 0
        for i in range(self.num_queens):
            for j in range(i + 1, self.num_queens):
                if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                    conflicts += 1
        return -conflicts  # Minimize conflicts, so we return negative conflicts

    def select(self):
        # Tournament selection
        tournament_size = 5
        tournament = random.sample(self.population, tournament_size)
        return max(tournament, key=self.fitness)

    def crossover(self(parent1, parent2):
        point = random.randint(0, self.num_queens - 1)
        return parent1[:point] + parent2[point:]

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            idx = random.randint(0, self.num_queens - 1)
            individual[idx] = random.randint(0, self.num_queens - 1)
        return individual

    def run(self):
        for generation in range(self.max_generations):
            new_population = []
            while len(new_population) < self.population_size:
                parent1 = self.select()
                parent2 = self.select()
                offspring = self.crossover(parent1, parent2)
                offspring = self.mutate(offspring)
                new_population.append(offspring)

            self.population = new_population
            best_individual = max(self.population, key=self.fitness)
            best_fitness = self.fitness(best_individual)
            
            print(f"Generation {generation + 1}: Best Fitness = {-best_fitness}")

            if best_fitness == 0:
                print("Solution Found:")
                print(best_individual)
                break

# Parameters
num_queens = 8
population_size = 100
mutation_rate = 0.05
max_generations = 1000

# Run Genetic Algorithm
ga = GeneticAlgorithmNQueens(num_queens, population_size, mutation_rate, max_generations)
ga.run()
