import numpy as np

def CreateChessBoardMatrix(n):

    ChessBoardMatrix = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            ChessBoardMatrix[i][j] = np.power(-1,i+j)

    return ChessBoardMatrix

CreateChessBoardMatrix(3)