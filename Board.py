class Board:
    def __init__(self, height = 10, width = 5):
        self.height = height
        self.width = width
        self.board = [["-"]* width]*height
    
    def get_cell(self,r,c):
        return self.board[r][c]
    
    def set_cell(self,r,c,val):
        self.board[r][c] = val

    def display_board(self):
        for r in range(self.height):
           print("\n")
           for c in range(self.width):
              print(self.board[r][c],end=" ")
                