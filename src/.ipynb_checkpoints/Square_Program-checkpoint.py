import multiprocessing
import concurrent.futures
import time
import random

# Function to compute square of a number
def square(num):
    return num * num

# Generate large test data
NUMBERS_1M = [random.randint(1, 1000) for _ in range(10**6)]
NUMBERS_10M = [random.randint(1, 1000) for _ in range(10**7)]

# Sequential Execution
def sequential_squares(numbers):
    start = time.time()
    results = [square(num) for num in numbers]
    end = time.time()
    print(f"Sequential Execution Time: {end - start:.4f} seconds")
    return results

# Multiprocessing with a process for each number
def multiprocessing_squares(numbers):
    start = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(square, numbers)
    end = time.time()
    print(f"Multiprocessing Execution Time: {end - start:.4f} seconds")
    return results

# Using concurrent.futures ProcessPoolExecutor
def process_pool_executor(numbers):
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        results = list(executor.map(square, numbers))
    end = time.time()
    print(f"ProcessPoolExecutor Execution Time: {end - start:.4f} seconds")
    return results

# Function to run all tests
def run_square_tests():
    print("Running tests for 10^6 numbers:")
    sequential_squares(NUMBERS_1M)
    multiprocessing_squares(NUMBERS_1M)
    process_pool_executor(NUMBERS_1M)

    print("\nRunning tests for 10^7 numbers:")
    sequential_squares(NUMBERS_10M)
    multiprocessing_squares(NUMBERS_10M)
    process_pool_executor(NUMBERS_10M)
