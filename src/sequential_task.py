import time  # Ensure time module is imported
from src.functions import generate_random_chars, generate_random_sum

# Function to run the sequential task
def run_sequential():
    # Measure time for generating random characters
    start_time = time.time()
    random_chars = generate_random_chars()  # Store the output
    end_time = time.time()
    print(f"Generated Characters: {random_chars}")
    print(f"Time to generate random characters (sequential): {end_time - start_time:.6f} seconds.")
    
    # Measure time for generating random sum
    start_time = time.time()
    random_sum = generate_random_sum(3, 5)  # Pass valid arguments
    end_time = time.time()
    print(f"Generated Sum: {random_sum}")
    print(f"Time to generate random sum (sequential): {end_time - start_time:.6f} seconds.")
