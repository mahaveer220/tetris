import Block
from Block import *
import copy
import time

class Board:
    def __init__(self, height = 20, width = 10):
        self.height = height
        self.width = width
        self.block = Block()
        self.present_height = 0
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
        print("\n\n\n")

    def clear_block(self, block):
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
            if c<0 or c>=self.width or r>=self.height or r<0 or self.board[r][c]==self.fill:
                return False
        return True


    def update_board(self, keystroke = None , block = None):
        next_position = self.block.move_block(block = block, keystroke=keystroke)
        down_position = self.block.move_block(block = block, keystroke= Keystroke().down )
        if self.is_position_safe(next_position):
            self.clear_block(block)
            self.put_block(next_position)
            return next_position
        
        elif self.is_position_safe(down_position):
            self.clear_block(block)
            self.put_block(down_position)
            return down_position
        
        return None
    
    def process_rows(self, indices):
        board  = []
        for idx in range(self.height):
            if idx in indices:
                continue
            board.append( self.board[idx][:] )
        
        n = len(indices)
        while n:
            board.insert(0, [self.empty for _ in range(self.width)] )
            n -= 1
        self.board = copy.deepcopy(board)




                