import Player
from Player import *

import Blocks
from Blocks import *

import Board
from Board import *

class Tetris:
    def __init__(self):
        self.player = self.initialize_player()
        self.board = self.initialize_board()
        self.game_alive = True
        self.player_input_timeout = 3 # 1 sec
        self.start_game()

    def initialize_player(self):
        player = Player()
        # player.ask_player_name()
        # print("Hello {}! Welcome to Tetris".format(player.get_player_name()))
        return player
    
    def initialize_board(self):
        board = Board(height = 8, width = 8)
        return board

    def wait_for_enter_key(self):
        print("Press Enter to start the game")
        input()
        print("Game Started")

    def pause_game(self):
        pass
    
    def start_game(self):
        self.wait_for_enter_key()
        while(self.game_alive):
            val = self.player.wait_for_input(self.player_input_timeout)
            if val=='':
                self.game_alive = False
            

        print("Game Stopped")

game = Tetris()

