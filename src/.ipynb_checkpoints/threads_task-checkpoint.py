import threading
import time  # Ensure time module is imported
from src.functions import generate_random_chars, generate_random_sum

# Function to wrap each task in a thread
def thread_function(func, *args):
    func(*args)  # Call the function inside the thread

# Function to run the threading task
def run_threads():
    # Start threads for both tasks
    thread1 = threading.Thread(target=thread_function, args=(generate_random_chars,))
    thread2 = threading.Thread(target=thread_function, args=(generate_random_sum, 3, 5))  # Fixed missing arguments
    
    # Run the threads
    start_time = time.time()  # Measure start time
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    
    end_time = time.time()  # Measure end time
    print(f"Time to execute using threads: {end_time - start_time:.6f} seconds.")
