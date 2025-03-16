Parallel and Distributed Computing - Assignment 1
Course: DSAI 3202
Author: [Your Name]
Date: [Assignment Submission Date]

1. Introduction
This project explores multiprocessing and process synchronization in Python.
It contains two implementations:

square_program.py – Computes squares of numbers using different parallel techniques.
connection_pool.py – Simulates a database connection pool using semaphores to control access.
2. Requirements
Python 3.8+
No external dependencies (only standard Python libraries)
3. How to Run
A. Running the Square Program
bash
Copy
Edit
python square_program.py
This script:

Generates a list of random numbers.
Computes their squares using:
Sequential processing
Multiprocessing (apply, map, apply_async)
concurrent.futures.ProcessPoolExecutor
Measures and compares execution times.
B. Running the Connection Pool Program
bash
Copy
Edit
python connection_pool.py
This script:

Creates a ConnectionPool with a limited number of connections.
Uses semaphores to ensure controlled access.
Simulates multiple processes requesting and releasing database connections.
4. Observations
A. Square Program Results
Multiprocessing significantly reduces execution time, especially for large datasets.
Pool.map() and ProcessPoolExecutor are the most efficient.
Sequential processing is the slowest.
B. Connection Pool Results
Semaphore ensures that only a fixed number of processes access connections at a time.
Processes wait when the pool is full, preventing race conditions.
5. Conclusion
This assignment demonstrates how Python multiprocessing improves performance and how semaphores help manage shared resources safely.

