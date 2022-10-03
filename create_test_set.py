from generator import generate_puzzles
from typing import List
from models.puzzle import Puzzle
from read_write import write_puzzles


puzzles: List[Puzzle] = []
puzzles += generate_puzzles(100, 4, 8)
puzzles += generate_puzzles(100, 4, 10)
puzzles += generate_puzzles(100, 4, 12)
puzzles += generate_puzzles(100, 5, 12)
puzzles += generate_puzzles(100, 5, 14)
puzzles += generate_puzzles(100, 5, 16)
puzzles += generate_puzzles(100, 6, 16)
puzzles += generate_puzzles(100, 6, 18)
puzzles += generate_puzzles(100, 6, 20)
write_puzzles(puzzles)