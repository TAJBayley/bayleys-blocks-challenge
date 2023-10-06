from models.puzzle import Puzzle
from solver import solve_puzzle_set, Method
from read_write import read_puzzles

def main():
    print("Welcome to Bayley's Blocks Challenge!")
    puzzles = read_puzzles()
    brute_force_time = solve_puzzle_set(puzzles, Method.BRUTE_FORCE)
    print("Time: {:.3f}s".format(brute_force_time))

    custom_method_time = solve_puzzle_set(puzzles, Method.CUSTOM)
    print("Time: {:.3f}s".format(custom_method_time))

    speed_improvement = brute_force_time / custom_method_time
    print("Custom method is {:.2f}x faster".format(speed_improvement))

if __name__ == "__main__":
    main()