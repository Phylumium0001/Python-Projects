class Cell:
    def __init__(self,is_mine=False,coord_x=0, cood_y=0) -> None:
        # Mine or Empty
        self.is_revealed = False
        self.is_mine = is_mine
        self.coordinate_x = coord_x
        self.coordinate_y = cood_y
        self.neighbouring_coordinates = {
            "N":[self.coordinate_x - 1,self.coordinate_y],
            "NE":[self.coordinate_x -1 ,self.coordinate_y + 1],
            "E":[self.coordinate_x,self.coordinate_y + 1],
            "SE":[self.coordinate_x + 1,self.coordinate_y+1],
            "S":[self.coordinate_x + 1,self.coordinate_y],
            "SW":[self.coordinate_x + 1,self.coordinate_y - 1],
            "W":[self.coordinate_x,self.coordinate_y - 1],
            "NW":[self.coordinate_x-1,self.coordinate_y - 1]
            }
        
        self.neighbouring_mines = 0


    def add_mine(self):
        self.is_mine = True
    
    def increment_neighbouring_mine_count(self):
        self.neighbouring_mines += 1


    def __str__(self) -> str:
        return f"Cell(Revealed : {self.is_revealed}, Is_mine : {self.is_mine},({self.coordinate_x},{self.coordinate_y}))"

    
    def __repr__(self) -> str:
        s = "R" if self.is_revealed else "H"
        v = "M" if self.is_mine else "S"

        # return f"({s},{v})"
        return f"({v},{self.neighbouring_mines})"
    
if __name__ == "__main__":
    cell1 = Cell()
    cell2 = Cell(is_mine=True)

