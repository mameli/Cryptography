import numpy as np

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

def minor(arr,i,j):
    # ith row, jth column removed
    return arr[np.array(range(i)+range(i+1,arr.shape[0]))[:,np.newaxis],
               np.array(range(j)+range(j+1,arr.shape[1]))]

def inverseMatrixMod26(matrix,m):
    pAdj = np.zeros((m, m)).astype(int)
    detModulo = modinv(np.rint(np.linalg.det(matrix) % 26).astype(int), 26)
    for i in range(m):
        for j in range(m):
            if (i + j) % 2 == 0:
                pAdj[i][j] = np.rint(np.linalg.det(minor(matrix,j,i)))
            else:
                pAdj[i][j] = -1 * np.rint(np.linalg.det(minor(matrix,j,i)))
    return detModulo * pAdj % 26