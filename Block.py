import random

import Keystroke
from Keystroke import *

class Block:
    def __init__(self) -> None:
        self.blocks = 10
        self.present_location = None
        self.keystroke = Keystroke()
    
    def get_random_block(self):
        rand_block = random.randint(1,2)
        if rand_block == 1:
            return [(0,2),(0,3),(0,4)]
        else:
            return [(0,3),(1,3),(2,3)]
            # return [(0,2),(0,3),(0,4)]
    

    def move_block(self, keystroke = None, block = None):
        if not block or not keystroke:
            return block
        res = []

        if keystroke == self.keystroke.down:
            for coord in block:
                x,y = coord
                res.append((x+1,y))

        elif keystroke == self.keystroke.left:
            for coord in block:
                x,y = coord
                res.append((x+1,y-1))
        
        elif keystroke == self.keystroke.right:
            for coord in block:
                x,y = coord
                res.append((x+1,y+1))
        
        elif keystroke == self.keystroke.rotate:
            px, py = block[1]
            for coord in block:
                x,y = coord
                x,y = x - px, y-py
                x,y = y,x
                x,y = x + py, y + px
                res.append((x,y))     

        return res

            


    

    