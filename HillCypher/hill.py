from itertools import permutations
from numpy.linalg import inv
from modInverse import modinv, inverseMatrixMod26
from utilMatrix import charToMatrix, matrixToChar
import numpy as np
import math
import sys


def detNotNUllSub(matrix, m):
    columns = ''
    for i in range(len(matrix[0])):
        columns += str(i)

    for x in permutations(columns, r=m):
        listCol = map(int, list(x))
        det = np.rint(np.linalg.det(matrix[:, listCol]) % 26)
        if det != 0 and modinv(det, 26) != -1:
            return listCol
    print "Non esiste una sottomatrice accettabile per ricavare la chiave"
    return -1


def crypt(pt, key):
    m = int(math.sqrt(len(key)))
    matKey = charToMatrix(key, m)
    matPt = charToMatrix(pt, m)
    return np.dot(matKey, matPt) % 26


def decrypt(ct, key):
    m = int(math.sqrt(len(key)))
    matKey = charToMatrix(key, m)
    detModulo26 = modinv(np.rint(np.linalg.det(matKey) % 26), 26)
    matKeyInv = np.rint(detModulo26 * inv(matKey) * np.linalg.det(matKey) % 26)
    matCt = charToMatrix(ct, m)
    return np.dot(matKeyInv, matCt) % 26


def cryptAnalysis(pt, ct, m):
    matPt = charToMatrix(pt, m)
    matCt = charToMatrix(ct, m)
    colInd = detNotNUllSub(matPt, m)
    if colInd == -1:
        return None
    detModulo26 = modinv(np.rint(np.linalg.det(matPt[:, colInd]) % 26), 26)
    matPtInv = inverseMatrixMod26(matPt[:, colInd], m)
    matPtInv = np.rint(
        detModulo26 * inv(matPt[:, colInd]) * np.linalg.det(matPt[:, colInd]) % 26)
    return np.dot(matCt[:, colInd], matPtInv) % 26

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:  # Crypt and Decrypt (plainText, key)
        print 'Hill ', args[1], ' result ', matrixToChar(locals()[args[1]](args[2], args[3]))
    if len(args) == 5:  # CryptAnalysis (plainText, cipherText, m)
        print 'Hill ', args[1], ' result ', matrixToChar(locals()[args[1]](args[2], args[3], int(args[4])))

# # Debug
# plainText = "friday"
# keyText = 'htid'
# m = int(math.sqrt(len(keyText)))
# print 'PlainText'
# print charToMatrix(plainText, m)
# print 'Key'
# print charToMatrix(keyText, m)
# print 'chiave in lettere: ', keyText
# # Crypt
# cipherMat = crypt(plainText, keyText)
# cipherText = matrixToChar(cipherMat)
# print 'testo cifrato: ', cipherText
# print cipherMat

# # Decrypt
# ptMat = decrypt(cipherText, keyText)
# ptText = matrixToChar(ptMat)
# print 'testo decifrato: ', ptText
# print ptMat

# # CryptAnalysis
# keyMat = cryptAnalysis(plainText, cipherText, int(math.sqrt(len(keyText))))
# print 'chiave ricavata:'
# print keyMat
# print 'chiave in lettere: \n', matrixToChar(keyMat)