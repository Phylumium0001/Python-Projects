from dataclasses import dataclass

@dataclass
class Chunk:
    arg1 : int
    arg2 : int
    operation : str

if __name__ == "__main__":
    chunk = Chunk(1,2,'*')
    print(chunk)