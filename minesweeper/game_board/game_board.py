from cell import Cell
import random
 
class Board:
    def __init__(self,dimension) -> None:
        self.dimension = dimension
        self.x,self.y = self.dimension
        # Generate the board using the dimensions
        self.board = []
        self.generate_board()
        
    def generate_board(self):
        # Use the dimensions to determine the size of board
        self.populate_board()
        self.add_mines()

    def populate_board(self):
        for i in range(self.x):
            inner_board = []

            for j in range(self.y):
                # Add cell to inner board
                inner_board.append(Cell())
            # Add inner board to main board
            self.board.append(inner_board)

    def add_mines(self):
        num_of_mines = self.x
        all_cell_indexes = [(i,j) for i in range(self.x) for j in range(self.y)]
        random.shuffle(all_cell_indexes)

        for i,j in all_cell_indexes[:num_of_mines]:
            print(i,j)
            self.board[i][j].add_mine() 
    
    def check_cell_neighbours(self):
        # Return the number adjacent mine cells
        pass

if __name__ == "__main__":
    board = Board((8,8))

    print(board.board)