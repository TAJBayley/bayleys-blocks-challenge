from typing import List
import random
from models.puzzle import Puzzle

def __get_index_from_row_col(row: int, col: int, size: int) -> int:
    if row > size - 1 or col > size - 1:
        print("ERROR: row or column out of bounds")
    return row * size + col

def __find_moves(current_block: int, excluded_blocks: List[int], size: int) -> List[int]:
    available_moves = []
    row = int(current_block / size)
    column = int(current_block % size)
    shifts = [
        [-2, 1],
        [-2, -1],
        [2, 1],
        [2, -1],
        [-1, -2],
        [1, -2],
        [-1, 2],
        [1, 2]
    ]
    for shift in shifts:
        if ((row + shift[0]) >= 0) and ((row + shift[0]) < size):
            if ((column + shift[1]) >= 0) and ((column + shift[1]) < size):
                move = __get_index_from_row_col(row + shift[0], column + shift[1], size)
                if move not in excluded_blocks:
                    available_moves.append(move)

    return available_moves

def __is_puzzle_in_list(blocks_to_compare: List[int], puzzles: List[Puzzle]) -> bool:
    blocks_to_compare.sort()
    for puzzle in puzzles:
        filled_blocks = puzzle.get_filled_blocks()
        filled_blocks.sort()
        if filled_blocks == blocks_to_compare:
            # print("Puzzle has already been generated")
            return True
    return False

def generate_puzzles(quantity: int, size: int, blocks_per_puzzle: int, start_seed = 1) -> List[Puzzle]:
    # trace out path
    puzzles: List[Puzzle] = []
    all_blocks = list(range(0,size * size))
    attempt_count = 0
    max_attempts = 1000000
    puzzle_count = 0
    keep_searching = True
    while keep_searching:
        rand = random.Random(start_seed + attempt_count)
        current_block = rand.choice(all_blocks)
        visited_blocks: List[int] = [current_block]
        attempt_count += 1
        while len(visited_blocks) < blocks_per_puzzle:
            available_moves = __find_moves(current_block, visited_blocks, size)
            if len(available_moves) != 0:
                current_block = rand.choice(available_moves)
                visited_blocks.append(current_block)
            else:
                # print("No more moves left")
                break
        if len(visited_blocks) == blocks_per_puzzle:
            is_puzzle_in_list = __is_puzzle_in_list(visited_blocks, puzzles)
            if not is_puzzle_in_list:
                puzzle = Puzzle(size, visited_blocks)
                puzzles.append(puzzle)
                puzzle_count += 1
        if len(puzzles) >= quantity or attempt_count >= max_attempts:
            keep_searching = False
    print("Number of attempts: {}".format(attempt_count))
    print("Number of puzzles generated: {}".format(len(puzzles)))
    return puzzles