from typing import List
from models.puzzle import Puzzle
import json

def read_puzzles(file_name = "puzzles") -> List[Puzzle]:
    puzzles: List[Puzzle] = []
    with open('{}.json'.format(file_name)) as infile:
        puzzles_dict: List[dict[int, List[int]]] = json.load(infile)
        for puzzle_dict in puzzles_dict:
            puzzle = Puzzle(puzzle_dict["size"], puzzle_dict["filled_blocks"])
            puzzles.append(puzzle)
    return puzzles

def write_puzzles(puzzles: List[Puzzle], file_name = "puzzles"):
    with open('{}.json'.format(file_name), 'w') as outfile:
        puzzles_list: List[dict[int, List[int]]] = []
        for puzzle in puzzles:
            puzzle_dict = {"size": puzzle.get_size(), "filled_blocks": puzzle.get_filled_blocks()}
            puzzles_list.append(puzzle_dict)
        json.dump(puzzles_list, outfile)