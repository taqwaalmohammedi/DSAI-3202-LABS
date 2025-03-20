import numpy as np
import pandas as pd
import os
from genetic_algorithms_functions import calculate_fitness, \
    select_in_tournament, order_crossover, mutate, \
    generate_unique_population


# Load the distance matrix from the 'src' folder
distance_matrix = pd.read_csv("data/city_distances_extended.csv").to_numpy()

# Parameters
num_nodes = distance_matrix.shape[0]
population_size = 10000
num_tournaments = 8
mutation_rate = 0.9
num_generations = 200
infeasible_penalty = 1e6
stagnation_limit = 5

# Generate initial population
np.random.seed(42)
population = generate_unique_population(population_size, num_nodes)

# Initialize variables for tracking stagnation
best_fitness = int(1e6)
stagnation_counter = 0

# Main GA loop
for generation in range(num_generations):
    fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])

    # Check for stagnation
    current_best_fitness = np.min(fitness_values)
    if current_best_fitness < best_fitness:
        best_fitness = current_best_fitness
        stagnation_counter = 0
    else:
        stagnation_counter += 1

    # Regenerate population if stagnation limit is reached
    if stagnation_counter >= stagnation_limit:
        print(f"Regenerating population at generation {generation} due to stagnation")
        best_individual = population[np.argmin(fitness_values)]
        population = generate_unique_population(population_size - 1, num_nodes)
        population.append(best_individual)
        stagnation_counter = 0
        continue

    # Selection, crossover, mutation
    selected = select_in_tournament(population, fitness_values)
    offspring = []
    for i in range(0, len(selected), 2):
        parent1, parent2 = selected[i], selected[i + 1]
        route1 = order_crossover(parent1[1:], parent2[1:])
        offspring.append([0] + route1)
    mutated_offspring = [mutate(route, mutation_rate) for route in offspring]

    # Replace worst individuals
    for i, idx in enumerate(np.argsort(fitness_values)[::-1][:len(mutated_offspring)]):
        population[idx] = mutated_offspring[i]

    # Ensure unique population
    unique_population = set(tuple(ind) for ind in population)
    while len(unique_population) < population_size:
        individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
        unique_population.add(tuple(individual))
    population = [list(individual) for individual in unique_population]

    # Print best fitness
    print(f"Generation {generation}: Best fitness = {current_best_fitness}")

# Final best solution
fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])
best_idx = np.argmin(fitness_values)
best_solution = population[best_idx]
print("Best Solution:", best_solution)
print("Total Distance:", calculate_fitness(best_solution, distance_matrix))
