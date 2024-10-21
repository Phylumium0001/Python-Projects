from dataclasses import dataclass

@dataclass
class Cell:
    def __init__(self,is_mine=False) -> None:
        # Mine or Empty
        self.is_revealed = False
        self.is_mine = is_mine

    def add_mine(self):
        self.is_mine = True
    
    def __str__(self) -> str:
        return f"Cell(Revealed : {self.is_revealed}, Is_mine : {self.is_mine})"
    
    def __repr__(self) -> str:
        if self.is_revealed:
            s = "R"
        else:
            s = "H"

        if self.is_mine:
            v = "M"
        else:
            v = "S"
        return f"({s},{v})"
    
if __name__ == "__main__":
    cell1 = Cell()
    cell2 = Cell(is_mine=True)

