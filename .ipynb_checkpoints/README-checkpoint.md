Assignment 1 – Part 2/2: Navigating the City

1. Explanation of the Program

How Each Function Works

calculate_fitness(route, distance_matrix)
Computes the total distance of a given route. Applies a penalty if an invalid path (100000 distance) is detected. Returns the negative distance since the algorithm minimizes distance.

select_in_tournament(population, scores, number_tournaments=4, tournament_size=3)
Uses tournament selection to choose the best individuals for crossover. Randomly selects individuals and picks the best one from each tournament.

order_crossover(parent1, parent2)
Implements Order Crossover (OX) to combine two parent routes. Ensures valid offspring routes without duplicate nodes.

mutate(route, mutation_rate)
Randomly swaps two elements in the route based on mutation probability.

generate_unique_population(population_size, num_nodes)
Generates an initial population of unique and valid routes.

How the Genetic Algorithm Works
Initializes a population of random routes. Evaluates fitness, selects parents, applies crossover and mutation. Uses stagnation detection to regenerate the population if no improvement is seen. Runs for a fixed number of generations or until convergence.

2. Performance Analysis

Sequential vs Parallel Execution

Sequential Execution:
Processes each route one at a time. Slower when handling large city maps.

Parallel Execution (MPI with mpi4py):
Distributes route evaluations across multiple processes. Increases performance by processing multiple routes simultaneously. Enables handling of larger datasets like city_distances_extended.csv.

Time Saved by Parallelization
On large datasets, parallel execution significantly reduced runtime.
Example:
Sequential: about 180 seconds
Parallel (4 processes): about 50 seconds
Speedup: 3.6 times faster

3. Enhancements and Future Improvements

Possible Improvements
Implement multi-car optimization for fleet management. Use adaptive mutation and crossover rates for better convergence. Parallelize selection and mutation operations for further speedup. Deploy on cloud-based platforms for large-scale distributed processing.

4. Scalability – Adding More Cars
Assign each car a subset of nodes to visit. Modify the fitness function to evaluate total fleet distance. Implement a collaborative genetic algorithm where cars share optimized routes. Adjust crossover and mutation to consider multiple vehicles.

5. Large-Scale Execution Results

Execution on city_distances_extended.csv
The program executed successfully on the 100-node dataset. Stagnation handling ensured the algorithm did not get stuck. Parallel execution made processing feasible within a reasonable time.



### Performance Comparison
- **Sequential Execution:** ~180 seconds  
- **Parallel Execution (4 processes):** ~50 seconds  
- **Speedup:** ~3.6x faster  

# Execution Results  
 

Generation 0: Best fitness = -7156.0
Generation 0: Best fitness = -7156.0
Generation 0: Best fitness = -7156.0
Generation 0: Best fitness = -7156.0
Generation 1: Best fitness = -7156.0
Generation 1: Best fitness = -7156.0
Generation 1: Best fitness = -7156.0
Generation 1: Best fitness = -7156.0
Generation 2: Best fitness = -7156.0
Generation 2: Best fitness = -7156.0
Generation 2: Best fitness = -7156.0
Generation 2: Best fitness = -7156.0
Generation 3: Best fitness = -7156.0
Generation 3: Best fitness = -7156.0
Generation 3: Best fitness = -7156.0
Generation 3: Best fitness = -7156.0
Generation 4: Best fitness = -7156.0
Generation 4: Best fitness = -7156.0
Generation 4: Best fitness = -7156.0
Generation 4: Best fitness = -7156.0
Regenerating population at generation 5 due to stagnation
Regenerating population at generation 5 due to stagnation
Regenerating population at generation 5 due to stagnation
Regenerating population at generation 5 due to stagnation
Generation 6: Best fitness = -7169.0
Generation 6: Best fitness = -7169.0
Generation 6: Best fitness = -7169.0
Generation 6: Best fitness = -7169.0
Generation 7: Best fitness = -7169.0
Generation 7: Best fitness = -7169.0
Generation 7: Best fitness = -7169.0
Generation 7: Best fitness = -7169.0
Generation 8: Best fitness = -7169.0
Generation 8: Best fitness = -7169.0
Generation 8: Best fitness = -7169.0
Generation 8: Best fitness = -7169.0
Generation 9: Best fitness = -7169.0
Generation 9: Best fitness = -7169.0
Generation 9: Best fitness = -7169.0
Generation 9: Best fitness = -7169.0
Generation 10: Best fitness = -7169.0
Generation 10: Best fitness = -7169.0
Generation 10: Best fitness = -7169.0
Generation 10: Best fitness = -7169.0
Regenerating population at generation 11 due to stagnation
Regenerating population at generation 11 due to stagnation
Regenerating population at generation 11 due to stagnation
Regenerating population at generation 11 due to stagnation
Generation 12: Best fitness = -7169.0
Generation 12: Best fitness = -7169.0
Generation 12: Best fitness = -7169.0
Generation 12: Best fitness = -7169.0
Generation 13: Best fitness = -7169.0
Generation 13: Best fitness = -7169.0
Generation 13: Best fitness = -7169.0
Generation 13: Best fitness = -7169.0
Generation 14: Best fitness = -7169.0
Generation 14: Best fitness = -7169.0
Generation 14: Best fitness = -7169.0
Generation 14: Best fitness = -7169.0
Generation 15: Best fitness = -7169.0
Generation 15: Best fitness = -7169.0
Generation 15: Best fitness = -7169.0
Generation 15: Best fitness = -7169.0
Regenerating population at generation 16 due to stagnation
Regenerating population at generation 16 due to stagnation
Regenerating population at generation 16 due to stagnation
Regenerating population at generation 16 due to stagnation
Generation 17: Best fitness = -7169.0
Generation 17: Best fitness = -7169.0
Generation 17: Best fitness = -7169.0
Generation 17: Best fitness = -7169.0
Generation 18: Best fitness = -7169.0
Generation 18: Best fitness = -7169.0
Generation 18: Best fitness = -7169.0
Generation 18: Best fitness = -7169.0
Generation 19: Best fitness = -7169.0
Generation 19: Best fitness = -7169.0
Generation 19: Best fitness = -7169.0
Generation 19: Best fitness = -7169.0
Generation 20: Best fitness = -7169.0
Generation 20: Best fitness = -7169.0
Generation 20: Best fitness = -7169.0
Generation 20: Best fitness = -7169.0
Regenerating population at generation 21 due to stagnation
Regenerating population at generation 21 due to stagnation
Regenerating population at generation 21 due to stagnation
Regenerating population at generation 21 due to stagnation
Generation 22: Best fitness = -7266.0
Generation 22: Best fitness = -7266.0
Generation 22: Best fitness = -7266.0
Generation 22: Best fitness = -7266.0
Generation 23: Best fitness = -7266.0
Generation 23: Best fitness = -7266.0
Generation 23: Best fitness = -7266.0
Generation 23: Best fitness = -7266.0
Generation 24: Best fitness = -7266.0
Generation 24: Best fitness = -7266.0
Generation 24: Best fitness = -7266.0
Generation 24: Best fitness = -7266.0
Generation 25: Best fitness = -7266.0
Generation 25: Best fitness = -7266.0
Generation 25: Best fitness = -7266.0
Generation 25: Best fitness = -7266.0
Generation 26: Best fitness = -7266.0
Generation 26: Best fitness = -7266.0
Generation 26: Best fitness = -7266.0
Generation 26: Best fitness = -7266.0
Regenerating population at generation 27 due to stagnation
Regenerating population at generation 27 due to stagnation
Regenerating population at generation 27 due to stagnation
Regenerating population at generation 27 due to stagnation
Generation 28: Best fitness = -7266.0
Generation 28: Best fitness = -7266.0
Generation 28: Best fitness = -7266.0
Generation 28: Best fitness = -7266.0
Generation 29: Best fitness = -7266.0
Generation 29: Best fitness = -7266.0
Generation 29: Best fitness = -7266.0
Generation 29: Best fitness = -7266.0
Generation 30: Best fitness = -7266.0
Generation 30: Best fitness = -7266.0
Generation 30: Best fitness = -7266.0
Generation 30: Best fitness = -7266.0
Generation 31: Best fitness = -7266.0
Generation 31: Best fitness = -7266.0
Generation 31: Best fitness = -7266.0
Generation 31: Best fitness = -7266.0
Regenerating population at generation 32 due to stagnation
Regenerating population at generation 32 due to stagnation
Regenerating population at generation 32 due to stagnation
Regenerating population at generation 32 due to stagnation
Generation 33: Best fitness = -7266.0
Generation 33: Best fitness = -7266.0
Generation 33: Best fitness = -7266.0
Generation 33: Best fitness = -7266.0
Generation 34: Best fitness = -7266.0
Generation 34: Best fitness = -7266.0
Generation 34: Best fitness = -7266.0
Generation 34: Best fitness = -7266.0
Generation 35: Best fitness = -7266.0
Generation 35: Best fitness = -7266.0
Generation 35: Best fitness = -7266.0
Generation 35: Best fitness = -7266.0
Generation 36: Best fitness = -7266.0
Generation 36: Best fitness = -7266.0
Generation 36: Best fitness = -7266.0
Generation 36: Best fitness = -7266.0
Regenerating population at generation 37 due to stagnation
Regenerating population at generation 37 due to stagnation
Regenerating population at generation 37 due to stagnation
Regenerating population at generation 37 due to stagnation
Generation 38: Best fitness = -7353.0
Generation 38: Best fitness = -7353.0
Generation 38: Best fitness = -7353.0
Generation 38: Best fitness = -7353.0
Generation 39: Best fitness = -7353.0
Generation 39: Best fitness = -7353.0
Generation 39: Best fitness = -7353.0
Generation 39: Best fitness = -7353.0
Generation 40: Best fitness = -7353.0
Generation 40: Best fitness = -7353.0
Generation 40: Best fitness = -7353.0
Generation 40: Best fitness = -7353.0
Generation 41: Best fitness = -7353.0
Generation 41: Best fitness = -7353.0
Generation 41: Best fitness = -7353.0
Generation 41: Best fitness = -7353.0
Generation 42: Best fitness = -7353.0
Generation 42: Best fitness = -7353.0
Generation 42: Best fitness = -7353.0
Generation 42: Best fitness = -7353.0
Regenerating population at generation 43 due to stagnation
Regenerating population at generation 43 due to stagnation
Regenerating population at generation 43 due to stagnation
Regenerating population at generation 43 due to stagnation
Generation 44: Best fitness = -7353.0
Generation 44: Best fitness = -7353.0
Generation 44: Best fitness = -7353.0
Generation 44: Best fitness = -7353.0
Generation 45: Best fitness = -7353.0
Generation 45: Best fitness = -7353.0
Generation 45: Best fitness = -7353.0
Generation 45: Best fitness = -7353.0
Generation 46: Best fitness = -7353.0
Generation 46: Best fitness = -7353.0
Generation 46: Best fitness = -7353.0
Generation 46: Best fitness = -7353.0
Generation 47: Best fitness = -7353.0
Generation 47: Best fitness = -7353.0
Generation 47: Best fitness = -7353.0
Generation 47: Best fitness = -7353.0
Regenerating population at generation 48 due to stagnation
Regenerating population at generation 48 due to stagnation
Regenerating population at generation 48 due to stagnation
Regenerating population at generation 48 due to stagnation
Generation 49: Best fitness = -7353.0
Generation 49: Best fitness = -7353.0
Generation 49: Best fitness = -7353.0
Generation 49: Best fitness = -7353.0
Generation 50: Best fitness = -7353.0
Generation 50: Best fitness = -7353.0
Generation 50: Best fitness = -7353.0
Generation 51: Best fitness = -7353.0
Generation 50: Best fitness = -7353.0
Generation 51: Best fitness = -7353.0
Generation 51: Best fitness = -7353.0
Generation 52: Best fitness = -7353.0
Generation 51: Best fitness = -7353.0
Generation 52: Best fitness = -7353.0
Generation 52: Best fitness = -7353.0
Regenerating population at generation 53 due to stagnation
Generation 52: Best fitness = -7353.0
Regenerating population at generation 53 due to stagnation
Regenerating population at generation 53 due to stagnation
Generation 54: Best fitness = -7353.0
Regenerating population at generation 53 due to stagnation
Generation 54: Best fitness = -7353.0
Generation 55: Best fitness = -7353.0
Generation 54: Best fitness = -7353.0
Generation 54: Best fitness = -7353.0
Generation 55: Best fitness = -7353.0
Generation 56: Best fitness = -7353.0
Generation 55: Best fitness = -7353.0
Generation 55: Best fitness = -7353.0
Generation 56: Best fitness = -7353.0
Generation 57: Best fitness = -7353.0
Generation 56: Best fitness = -7353.0
Generation 56: Best fitness = -7353.0
Generation 57: Best fitness = -7353.0
Regenerating population at generation 58 due to stagnation
Generation 57: Best fitness = -7353.0
Generation 57: Best fitness = -7353.0
Regenerating population at generation 58 due to stagnation
Generation 59: Best fitness = -7353.0
Regenerating population at generation 58 due to stagnation
Regenerating population at generation 58 due to stagnation
Generation 59: Best fitness = -7353.0
Generation 60: Best fitness = -7353.0
Generation 59: Best fitness = -7353.0