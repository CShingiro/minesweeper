import mine
import point

class Board:
    def __init__(self, board_length,board_height):
        self.board = []
        for i in range(board_length):
            self.board.append([])
            for j in range(board_height):
                self.board[i][j] = 0
        
    
    def __repr__(self):
        return self.board


test_board = Board(9,5)
test_board