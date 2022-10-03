import copy
import time
from typing import List, Tuple
from models.puzzle import Puzzle
from helper import print_progress_bar

def solve_puzzle_set(puzzles: List[Puzzle]) -> int:
    start_time = time.time()
    print_progress_bar(0, len(puzzles), prefix = 'Solving Puzzles:', suffix = 'Complete', length = 50)
    for i, puzzle in enumerate(puzzles):
        solve_puzzle(puzzle)
        print_progress_bar(i + 1, len(puzzles), prefix = 'Solving Puzzles:', suffix = 'Complete', length = 50)
    total_time = time.time() - start_time
    return total_time

def solve_puzzle(puzzle: Puzzle) -> Tuple[List[int], bool]:
    # create a deep copy of the puzzle
    puzzle_copy = copy.deepcopy(puzzle)

    # ************* add implementation here  *************
    route, solved = brute_force_method(puzzle_copy)
    # ****************************************************
    
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
    
