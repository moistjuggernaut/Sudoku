import numpy as np

class Board:
    def __init__(self, assignment):
        self.assignment = assignment


x = Board(np.zeros(7))
print(x.assignment)
