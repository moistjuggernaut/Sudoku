import numpy as np
from numpy.lib.shape_base import column_stack

class Board:
    def __init__(self, assignment):
        self.assignment = assignment


ex1 = np.array(
[[3, 4, np.nan , 2, 9, 8, 7, np.nan, 1],
[9,6,np.nan, np.nan, 5, np.nan, np.nan, np.nan, np.nan],
[8,7, np.nan,6, np.nan,1,5,9,3],
[1, np.nan, np.nan, np.nan, 2, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, 7, 8, np.nan, np.nan, np.nan, 4, 9],
[5, np.nan, 8, np.nan, np.nan, np.nan, 1, np.nan, 6],
[np.nan, np.nan, 9, np.nan, np.nan, np.nan, 4, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, 7, 2, np.nan, 1, 5],
[7, np.nan, np.nan, 1, np.nan, 4, np.nan, np.nan, np.nan]])


values = np.isnan(ex1)
row_sum = values.sum(axis=0)
col_sum = values.sum(axis=1).reshape(9,1)

def sqSum(matrix):
    row_sum = []
    col_sum = []
    for i in range(0, 9, 3):
        row_sum = np.append(row_sum, matrix[i:i+3,i:i+3].sum(axis=0))
        col_sum = np.append(col_sum, matrix[i:i+3,i:i+3].sum(axis=1))
    return row_sum + col_sum.reshape(9,1)



result = row_sum + col_sum + sqSum(values)
print(result.index(min(result)))