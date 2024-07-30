from typing import List, Tuple
from Model.PlayingPiece import PlayingPiece

class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def add_piece(self, row: int, column: int, playing_piece: PlayingPiece) -> bool:
        if self.board[row][column] is not None:
            return False
        self.board[row][column] = playing_piece
        return True

    def get_free_cells(self) -> List[Tuple[int, int]]:
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    free_cells.append((i, j))
        return free_cells

    def print_board(self):
        for i in range(self.size):
            row_elements = []
            for j in range(self.size):
                if self.board[i][j] is not None:
                    row_elements.append(self.board[i][j].piece_type.value)
                else:
                    row_elements.append(" ")
            print(" | ".join(row_elements))
            if i < self.size - 1:
                print("-" * (4 * self.size - 1))