import random

import Keystroke
from Keystroke import *

class Block:
    def __init__(self) -> None:
        self.blocks = 10
        self.present_location = None
        self.keystroke = Keystroke()
    
    def get_random_block(self):
        # return random.randint(1,10)
        return [(0,2),(0,3),(0,4)]
    

    def move_block(self, keystroke = None, block = None):
        if not block or not keystroke:
            return block
        res = []
        if keystroke == self.keystroke.down:
            for coord in block:
                x,y = coord
                res.append((x+1,y))
        return res

            


    

    