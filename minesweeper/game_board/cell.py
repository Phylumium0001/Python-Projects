from dataclasses import dataclass

@dataclass
class Cell:
    def __init__(self,is_mine=False) -> None:
        # Mine or Empty
        self.is_revealed = False
        self.is_mine = is_mine

if __name__ == "__main__":
    cell1 = Cell()
    cell2 = Cell(is_mine=True)
    
