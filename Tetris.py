import Player
from Player import *

import Block
from Block import *

import Board
from Board import *

import Keystroke
from Keystroke import *

import os, time, sys

class Tetris:
    def __init__(self):
        self.player = self.initialize_player()
        self.board = self.initialize_board()
        self.keystroke = Keystroke()
        self.present_block = Block().get_random_block()
        self.next_block = Block().get_random_block()
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
        # self.wait_for_enter_key()
        while(self.game_alive):
            # display board
            self.board.display_board()
            keystroke = self.player.wait_for_input(self.player_input_timeout)
            # quit game 
            if keystroke == self.keystroke.quit:
                self.game_alive = False
                sys.exit()

            # updating board with keystroke and update the block
            self.present_block = self.board.update_board( keystroke = keystroke , block = self.present_block)
            self.board.display_board()

            # assign blocks for next frame 
            # self.present_block = self.next_block
            # self.next_block = Block().get_random_block()
            # print("Present:", self.present_block)
            # print("Random:", self.next_block)

            time.sleep(1)
            os.system("clear")
            
        print("Game Stopped")

game = Tetris()

