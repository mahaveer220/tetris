import random

class Blocks:
    def __init__(self) -> None:
        self.blocks = 10
    
    def get_random_block(self):
        return random.uniform(1,10)

    