from game_board.cell import Cell
import random
 
class Board:
    def __init__(self,dimension) -> None:
        self.dimension = dimension
        self.x,self.y = self.dimension

        self.mines = []

        # Generate the board using the dimensions
        self.board = []
        self.generate_board()
        
    def generate_board(self):
        # Use the dimensions to determine the size of board
        self.populate_board()
        self.add_mines()
        self.update_mine_neighbours()

    def populate_board(self):
        for i in range(self.x):
            inner_board = []

            for j in range(self.y):
                # Add cell to inner board
                inner_board.append(Cell(coord_x=i,cood_y=j))
            # Add inner board to main board
            self.board.append(inner_board)

    def add_mines(self):
        num_of_mines = self.x
        all_cell_indexes = [(i,j) for i in range(self.x) for j in range(self.y)]
        random.shuffle(all_cell_indexes)

        for i,j in all_cell_indexes[:num_of_mines]:
            self.mines.append(self.board[i][j])
            self.board[i][j].add_mine() 
    
    def update_mine_neighbours(self):
        """
        Makes all the cells aware of their neighbours if they are mines
        """
        for mine in self.mines:
            for coordinate in mine.neighbouring_coordinates.values():
                # Check border case
                x,y = coordinate
                if x >= 0 and x < self.x and y >= 0 and y < self.y:
                    
                    # Cell exists
                    self.board[x][y].increment_neighbouring_mine_count()

if __name__ == "__main__":
    board = Board((8,8))
    print(board.board)