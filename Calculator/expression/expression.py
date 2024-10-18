from dataclasses import dataclass
from chunk import Chunk

class Expression:
    expression : str
    simplified_expression = ""


    def simplify_simple(self):
        # Apply BODMAS to split the expression into chunks
        # Check for the prescence of all the operations
        #  and update the final chunk
        pass

    def simplify_complex(self):
        pass
