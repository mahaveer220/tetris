import Block
from Block import *
import copy

class Board:
    def __init__(self, height = 10, width = 5):
        self.height = height
        self.width = width
        self.block = Block()
        self.can_change = True
        self.empty = "-"
        self.fill = "*"
        self.board = [[self.empty for _ in range(width)] for _ in range(height)]
    
    def get_cell(self,r,c):
        return self.board[r][c]
    
    def set_cell(self,r,c,val):
        self.board[r][c] = val

    def display_board(self):
        for r in range(self.height):
           print("\n")
           for c in range(self.width):
              print(self.board[r][c],end=" ")

    def can_change():
        return self.can_change

    def clear_block(self, block):
        board = self.board.copy()
        for t in block:
            r,c = t
            self.board[r][c] = self.empty
    
    def put_block(self, block):
        for t in block:
            r,c = t
            self.board[r][c] = self.fill
    
    def is_position_safe(self, block):
        for t in block:
            r,c = t
            if self.board[r][c]==self.fill:
                return False
        return True


    def update_board(self, keystroke = None , block = None):
        next_position = self.block.move_block(block = block, keystroke=keystroke)
        if self.is_position_safe(next_position):
            self.clear_block(block)
            self.put_block(next_position)
        else:
            return block
        return next_position

                