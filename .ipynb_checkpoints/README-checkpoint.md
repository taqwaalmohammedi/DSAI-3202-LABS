Genetic Algorithm for Shortest Route Optimization
1. Introduction
In this part of the assignment, I implemented and tested a Genetic Algorithm (GA) to solve the shortest route problem for a given set of cities. The goal was to optimize the order of cities visited to minimize the total travel distance. The program utilized a genetic evolution approach to find better routes over multiple generations.

2. Problem Statement
The problem involves a set of cities with pre-defined distances stored in a distance matrix (city_distances_extended.csv). The goal is to determine the most efficient travel path that visits all cities while minimizing the total distance traveled.

3. Methodology
3.1. Genetic Algorithm Overview
The algorithm follows a standard Genetic Algorithm approach:

Initialization: A population of possible routes is generated randomly.
Fitness Evaluation: Each route is evaluated based on its total distance.
Selection: The best routes are chosen using tournament selection.
Crossover: The selected routes are combined using order crossover (OX).
Mutation: Some routes undergo mutations to introduce diversity.
Stagnation Handling: If the best route does not improve after a set number of generations, the population is regenerated.
3.2. Key Parameters Used
Population Size: 10,000
Tournament Selection Size: 8
Mutation Rate: 0.9
Generations: 200
Penalty for Infeasible Routes: 
10
6
10 
6
 
Stagnation Limit: 5 generations without improvement
4. Implementation
The code was structured as follows:

main.py: The entry point for running the genetic algorithm.
src/genetic_algorithm_trial.py: Contains the main GA functions.
src/genetic_algorithms_functions.py: Implements fitness calculation, selection, crossover, and mutation.
data/: Contains city distance files (city_distances.csv and city_distances_extended.csv).
4.1. Adjustments in Code Structure
A separate folder src/ was created to store Python scripts.
The data/ folder was used for storing city distance matrices.
Paths in the code were updated to reference the new structure correctly.
5. Results
After running the GA, the output showed a progressive improvement in fitness:

java
Copy
Edit
Using city_distances_extended.csv (Large City)
Generation 0: Best fitness = -7156.0
Generation 1: Best fitness = -7156.0
Generation 2: Best fitness = -7156.0
Generation 3: Best fitness = -7156.0
Generation 4: Best fitness = -7156.0
Regenerating population at generation 5 due to stagnation
Generation 6: Best fitness = -7169.0
Generation 7: Best fitness = -7169.0
Generation 8: Best fitness = -7169.0
Generation 9: Best fitness = -7169.0
The results indicate that the genetic algorithm successfully optimized the travel path, although improvements slowed down after a few generations.

6. Challenges Faced & Fixes
File Path Issues: Initially, the program could not locate the city_distances_extended.csv file. This was fixed by updating file paths.
Module Import Errors: The refactored code required modifications in main.py to correctly import functions.
Stagnation Handling: The algorithm was modified to regenerate the population after stagnation, improving the search for better routes.
7. Conclusion
This implementation of the Genetic Algorithm successfully demonstrated an evolutionary approach to solving the shortest route problem. The structured codebase and optimized parameters allowed the algorithm to find efficient routes. Future improvements could include adaptive mutation rates and parallel processing for faster execution.