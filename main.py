from generator import generate_puzzles
from typing import List
from models.puzzle import Puzzle
from solver import solve_puzzle_set
from read_write import write_puzzles, read_puzzles

def main():
    print("Welcome to Bayley's Blocks Challenge!")
    puzzles = read_puzzles()
    cycles, elapsed_time = solve_puzzle_set(puzzles)
    print("Time: {:.3f}s, Cyles: {:,}".format(elapsed_time, cycles))
    
if __name__ == "__main__":
    main()