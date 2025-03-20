import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


from src.genetic_algorithm_trial import run_genetic_algorithm

if __name__ == "__main__":
    run_genetic_algorithm()
