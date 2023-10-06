import copy
import sys
import time
from typing import List, Tuple
from models.puzzle import Puzzle
from helper import print_progress_bar
from enum import Enum

class Method(Enum):
    BRUTE_FORCE = 1
    CUSTOM = 2

def solve_puzzle_set(puzzles: List[Puzzle], method: Method) -> int:
    start_time = time.time()
    if method == Method.BRUTE_FORCE:
        prefixStr = "Solving Puzzles With Brute Force Method:"
    else:
        prefixStr = "Solving Puzzles With Custom Method:"
    print_progress_bar(0, len(puzzles), prefix = prefixStr, suffix = 'Complete', length = 50)
    for i, puzzle in enumerate(puzzles):
        solve_puzzle(puzzle, method)
        print_progress_bar(i + 1, len(puzzles), prefix = prefixStr, suffix = 'Complete', length = 50)
    total_time = time.time() - start_time
    return total_time

def solve_puzzle(puzzle: Puzzle, method: Method) -> Tuple[List[int], bool]:
    # create a deep copy of the puzzle
    puzzle_copy = copy.deepcopy(puzzle)

    if method == Method.BRUTE_FORCE:
        route, _ = brute_force_method(puzzle_copy)
    elif method == Method.CUSTOM:
        route = custom_method(puzzle_copy)

    solved = puzzle_copy.solved()
    if not solved:
        print("The puzzle was not solved successfully. Exiting Program.")
        sys.exit(0)
    return route, solved

def brute_force_method(puzzle: Puzzle) -> Tuple[List[int], bool]:
    available_moves = puzzle.get_available_moves()
    if len(available_moves) > 0:
        for move in available_moves:
            puzzle.make_move(move)
            visited_blocks, solved = brute_force_method(puzzle)
            if solved:
                return visited_blocks, solved
            puzzle.undo_move()
        return visited_blocks, solved
    return puzzle.get_visited_blocks(), puzzle.solved()

def custom_method(puzzle: Puzzle) -> Tuple[List[int], bool]:
    # ********** Replace with your method here ***********
    
    # ************ Then remove this section **************
    print("Custom method has not yet been implemented. Exiting Program.")
    sys.exit(0)
    # ****************************************************
    return puzzle.get_visited_blocks()
    
