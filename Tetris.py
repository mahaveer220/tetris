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
        board = Board(height = 7, width = 6)
        return board

    def wait_for_enter_key(self):
        print("Press Enter to start the game")
        input()
        print("Game Started")

    def pause_game(self):
        pass
    

    def is_game_over(self):
        min_h = self.board.height
        for i in range(self.board.height):
            for j in range(self.board.width):
                if self.board.get_cell(i,j) == self.board.fill:
                    min_h = i
                    break
        return min_h<=1


    def process_rows(self):
        indices = []
        for row in range(self.board.height):
            count = 0
            for col in range(self.board.width):
                if self.board.get_cell(row, col) == self.board.fill:
                    count += 1
            if count==self.board.width:
                indices.append(row)

        self.board.process_rows(indices)
        

    def start_game(self):
        self.board.display_board()
        # self.wait_for_enter_key()
        # os.system("clear")
        while(self.game_alive):
            # display board

            keystroke = self.player.wait_for_input(self.player_input_timeout)
            # quit game 
            if keystroke == self.keystroke.quit:
                self.game_alive = False
                sys.exit()

            # updating board with keystroke and update the block
            os.system("clear")
            self.present_block = self.board.update_board( keystroke = keystroke , block = self.present_block)
            self.board.display_board()

            # make rows vanish
            self.process_rows()
    
            # assign blocks for next frame 
            if not self.present_block:
                # if self.is_game_over():
                #     print("Game Over !")
                #     sys.exit()
                self.present_block = self.next_block
                self.next_block = Block().get_random_block()
                print("\nPresent:", self.present_block)
                print("\nRandom:", self.next_block)

            time.sleep(1)

        print("Game Over")

game = Tetris()

