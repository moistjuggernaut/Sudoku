import numpy as np
from numpy.core.numeric import isfortran
from numpy.matrixlib.defmatrix import matrix


ex1 = np.array(
[
[3, 4, 0, 2, 9, 8, 7, 0, 1],
[9, 6, 0, 0, 5, 0, 0, 0, 0],
[8, 7, 0, 6, 0, 1, 5, 9, 3],
[1, 0, 0, 0, 2, 0, 0, 0, 0],
[0, 0, 7, 8, 0, 0, 0, 4, 9],
[5, 0, 8, 0, 0, 0, 1, 0, 6],
[0, 0, 9, 0, 0, 0, 4, 0, 0],
[0, 0, 0, 0, 7, 2, 0, 1, 5],
[7, 0, 0, 1, 0, 4, 0, 0, 0]])


def CalculateScore(matrix):
    test = np.zeros((9,9))

    for i in range(0, 9, 3):
        for j in range(0, 9,3 ):
            test[i:i+3,j:j+3] = matrix[i:i+3,j:j+3].sum()
    return test


isFound = (ex1 == 0)
row_sum = isFound.sum(axis=0)
col_sum = isFound.sum(axis=1).reshape(9,1)

result = (row_sum + col_sum + CalculateScore(isFound)) * isFound
nextToDetermine = np.unique(result)[1]
print(nextToDetermine)
indexOfNext = np.where(result == nextToDetermine)
i = indexOfNext[0][0]
j = indexOfNext[1][0]

def FindMissingNumber(i, j):
    for num in range(1,9):
        if num not in ex1[i,:]:
            if num not in (ex1[:,j]): #ook nog checken wel kwadrant
                print("found the number " + str(num) + " at position " + str(i) + " " + str(j))
                ex1[i,j] = num

    return ex1

FindMissingNumber(i,j)

## ik hou nog geen rekening met het feit dat je ook naar andere lijnen/ kolommen moet kijken naast diegene waar je in zit