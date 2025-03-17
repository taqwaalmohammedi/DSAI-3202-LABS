import sys
import os

# Ensure 'src' is in the import path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from Process import run_process
from Square_Program import run_square_tests

if __name__ == "__main__":
    print("Starting Process Simulation...")
    run_process()

    print("\nStarting Square Computation Tests...")
    run_square_tests()
