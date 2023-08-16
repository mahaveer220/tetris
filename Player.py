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

    # def wait_for_input(self, timeout):
    #     start_time = time.time()
    #     while time.time() - start_time < timeout:
    #         input_value = input('Enter some input: ')
    #         if input_value:
    #             return input_value
    #     else:
    #         print('timedout : moving block down')
    #         return None
        
    def wait_for_input(self, timeout):
        try:
            keystroke = inputimeout(prompt='Enter Input', timeout=timeout)
        except TimeoutOccurred:
            return 'd'
        return keystroke
