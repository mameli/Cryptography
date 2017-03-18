import numpy as np

def charToMatrix(text, m):
    # append x char to fit m formatting
    if len(text) % m != 0:
        text += 'x' * (m - len(text) % m)
    iText = []
    for c in text:
        iText.append(ord(c) - 97)
    matrixText = np.zeros((len(text) / m, m )).astype(int)
    tempBlock = []
    i = 0
    t = 0
    while i < len(iText):
        for k in range(i, m + i):
            tempBlock.append(iText[k])
        matrixText[t] = np.array(tempBlock[i : i + m])
        i = i + m
        t = t + 1
    return matrixText.T

def matrixToChar(matrixInt):
    text = ''
    for i in range(len(matrixInt[0])):
        for j in range(len(matrixInt)):
            text += str(unichr(matrixInt[j][i].item()+97))
    return text