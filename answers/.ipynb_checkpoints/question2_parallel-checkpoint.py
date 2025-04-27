import time
import multiprocessing
from src.maze import create_maze
from src.explorer import Explorer

def run_explorer(index):
    # Create a static maze using the helper function
    maze = create_maze(width=0, height=0, maze_type="static")  # width/height are ignored for static
    explorer = Explorer(maze, visualize=False)
    time_taken, moves = explorer.solve()
    return {
        "explorer_id": index,
        "time": round(time_taken, 6),
        "moves": len(moves)
    }

def main():
    num_explorers = 4
    with multiprocessing.Pool(processes=num_explorers) as pool:
        results = pool.map(run_explorer, range(num_explorers))

    print("\n=== Parallel Maze Explorer Results ===")
    for result in results:
        print(f"Explorer {result['explorer_id']} -> Time: {result['time']}s, Moves: {result['moves']}")
    
    best = min(results, key=lambda x: x['moves'])
    print(f"\n🎯 Best Explorer: #{best['explorer_id']} with {best['moves']} moves in {best['time']}s")
    print("======================================")

if __name__ == "__main__":
    main()
