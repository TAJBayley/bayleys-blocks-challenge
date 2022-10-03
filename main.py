from models.puzzle import Puzzle
from solver import solve_puzzle_set
from read_write import read_puzzles

def main():
    print("Welcome to Bayley's Blocks Challenge!")
    puzzles = read_puzzles()
    elapsed_time = solve_puzzle_set(puzzles)
    print("Time: {:.3f}s".format(elapsed_time))
    
if __name__ == "__main__":
    main()