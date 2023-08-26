import time
import sys
from inputimeout import inputimeout, TimeoutOccurred

class Player:
    def __init__(self, name=None):
        self.name = name
        self.level = 0

    def display_player_details(self):
        print("---------------")
        print("Player : ",self.name)
        print("Level  : ",self.level)
        print("---------------")
    
    def increase_level(self):
        self.level+=1
    
    def get_level(self):
        return self.level

    def get_player_name(self):
        return self.name
    
    def set_player_name(self,name):
        self.name = name

    def ask_player_name(self):
        print("Enter Player Name: ")
        name = input()
        self.set_player_name(name)

    def wait_for_input(self, timeout):
        # l -> move left
        # r -> move right
        # space -> rotate
        # no input in timelimit = d -> move down
      
        try:
            keystroke = inputimeout(prompt='\n\n Enter Input :', timeout=timeout)
        except TimeoutOccurred:
            return 'd'
        return keystroke
 