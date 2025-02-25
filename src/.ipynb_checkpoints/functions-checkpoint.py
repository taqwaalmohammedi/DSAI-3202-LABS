import multiprocessing
import time  # Ensure time module is imported

# Function to wrap each task in a process
def process_function(func, *args):
    return func(*args)

# Function to run the processes task
def run_processes():
    from src.functions import generate_random_chars, generate_random_sum  # Import inside function

    # Start processes for both tasks
    process1 = multiprocessing.Process(target=process_function, args=(generate_random_chars,))
    process2 = multiprocessing.Process(target=process_function, args=(generate_random_sum, 2, 3))  # Pass args correctly
    
    # Run the processes
    start_time = time.time()  # Measure start time
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
    
    end_time = time.time()  # Measure end time
    print(f"Time to execute using processes: {end_time - start_time} seconds.")
