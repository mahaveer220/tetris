import Player
from Player import *

import Blocks
from Blocks import *

import Board
from Board import *

class Tetris:
    def __init__(self):
        # self.player = self.initialize_player()
        # self.board = self.initialize_board()
        self.start_game()

    def initialize_player(self):
        player = Player()
        player.ask_player_name()
        # greet player
        print("Hello {}! Welcome to Tetris".format(player.get_player_name()))
        return player
    
    def initialize_board(self):
        board = Board(height = 8, width = 8)
        board.display_board()
        return board

    def wait_for_enter_key(self):
        print("Press Enter to start the game")
        input()
        print("game started")

    def start_game(self):
        self.wait_for_enter_key()
        

    

    
game = Tetris()

