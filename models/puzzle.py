from typing import List
import time

class Puzzle:
    def __init__(self, size: int, filled_blocks: List[int]):
        self.__size = size
        self.__filled_blocks = filled_blocks
        self.__visited_blocks = []
        self.__current_position = None

    # action functions

    def make_move(self, move: int) -> bool:
        available_moves = self.__find_available_moves()
        success = False
        if (move in available_moves):
            self.__current_position = move
            self.__visited_blocks.append(move)
            success = True
        return success

    def undo_move(self) -> bool:
        success = False
        if len(self.__visited_blocks) > 0:
            success = True
            del self.__visited_blocks[-1]
            if len(self.__visited_blocks) == 0:
                self.__current_position = None
            else:
                self.__current_position = self.__visited_blocks[-1]
        return success

    def any_moves_to_make(self) -> bool:
        available_moves = self.__find_available_moves()
        status = False
        if len(available_moves) > 0:
            return True
        return status

    def get_available_moves(self) -> List[int]:
         return self.__find_available_moves()

    def solved(self) -> bool:
        solved = False
        if len(self.__visited_blocks) == len(self.__filled_blocks):
            solved = True
        return solved

    # getters

    def get_size(self) -> int:
        return self.__size

    def get_filled_blocks(self) -> List[int]:
        return self.__filled_blocks

    def get_visited_blocks(self) -> List[int]:
        return self.__visited_blocks

    def get_current_position(self) -> int:
        if self.__current_position == None:
            print("No block yet selected")
        return self.__current_position

    def get_empty_blocks(self) -> List[int]:
        all_blocks: List[int] = list(range(0, self.__size * self.__size))
        return list(set(all_blocks) - set(self.__filled_blocks))

    # private functions

    def __find_available_moves(self) -> List[int]:
        available_moves = []
        if self.__current_position == None:
            if len(self.__visited_blocks) != 0:
                print("ERROR: If there are visited blocks a current position should exist")
            available_moves = self.__filled_blocks
        else:
            row = self.__get_current_row()
            column = self.__get_current_column()
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
                if ((row + shift[0]) >= 0) and ((row + shift[0]) < self.__size):
                    if ((column + shift[1]) >= 0) and ((column + shift[1]) < self.__size):
                        move = self.__get_index_from_row_col(row + shift[0], column + shift[1])
                        if move not in self.get_empty_blocks() and move not in self.get_visited_blocks():
                            available_moves.append(move)

        return available_moves
    
    def __get_index_from_row_col(self, row: int, col: int):
        if row > self.__size - 1 or col > self.__size - 1:
            print("ERROR: row or column out of bounds")
        return row * self.__size + col

    def __get_current_row(self):
        return int(self.__current_position / self.__size)

    def __get_current_column(self):
        return int(self.__current_position % self.__size)
    
    def display_grid(self, show_time=1):
        self.__print_grid()
        time.sleep(show_time)
        self.__un_print_grid()

    def __print_grid(self):
        chars_per_block = len(str(len(self.__filled_blocks)))
        grid = ""
        for i in range(0, self.__size):
            grid += "+"
            for j in range(0, self.__size):
                for _ in range(0, 2 + chars_per_block):
                    grid += "-"
                grid += "+"
            grid += "\n|"
            for j in range(0, self.__size):
                idx = self.__get_index_from_row_col(i, j)
                if idx in self.__visited_blocks:
                    grid += "·"
                    order_of_appearance = self.__visited_blocks.index(idx) + 1
                    grid += str(order_of_appearance)
                    for _ in range(0, 1 + chars_per_block - len(str(order_of_appearance))):
                        grid += "·"
                elif idx in self.__filled_blocks:
                    grid += "·"
                    grid += "·"
                    for _ in range(0, chars_per_block):
                        grid += "·"
                else:
                    grid += " "
                    for _ in range(0, 1 + chars_per_block):
                        grid += " "
                grid += "|"
            grid += "\n"
            for _ in range(0, chars_per_block - 1):
                grid += "|"
                for j in range(0, self.__size):
                    idx = self.__get_index_from_row_col(i, j)
                    if idx in self.__visited_blocks or idx in self.__filled_blocks:
                        for _ in range(0, 2 + chars_per_block):
                                grid += "·"
                    else:
                        for _ in range(0, 2 + chars_per_block):
                                grid += " "
                    grid += "|"
                grid += "\n"
        grid += "+"
        for j in range(0, self.__size):
            for _ in range(0, 2 + chars_per_block):
                grid += "-"
            grid += "+"
        print(grid)
        return
    
    def __un_print_grid(self):
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
        return_string = ""
        chars_per_block = len(str(len(self.__filled_blocks)))
        for _ in range(0, (1 + chars_per_block) * self.__size + 1):
            return_string += LINE_UP + LINE_CLEAR
        print(return_string, end="")
        return
    



