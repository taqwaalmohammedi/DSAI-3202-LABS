import sys
import os

# Add the 'src' directory to Python's module search path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Now, import from `src/`
from src.genetic_algorithm_trial import run_genetic_algorithm

if __name__ == "__main__":
    run_genetic_algorithm()
