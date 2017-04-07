from collections import Counter
from operator import itemgetter
import string
import sys
from itertools import cycle

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(key, ciphertext):
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result


def getCharFrequences(c):
    content = c
    listChars = Counter(content).most_common()
    d = dict.fromkeys(string.ascii_uppercase, 0)
    for c in listChars:
        d[c[0]] = float(c[1])
    return d

cypherText = filter(str.isalpha, open(sys.argv[2]).read())
print 'Numero di char ', len(cypherText)
m = int(sys.argv[1])
p = {'A': 0.081, 'B': 0.014, 'C': 0.027, 'D': 0.042, 'E': 0.127, 'F': 0.022, 'G': 0.02,
     'H': 0.06, 'I': 0.069, 'J': 0.001, 'K': 0.007, 'L': 0.04, 'M': 0.024, 'N': 0.067, 'O': 0.075,
     'P': 0.019, 'Q': 0.001, 'R': 0.060, 'S': 0.063, 'T': 0.09, 'U': 0.027, 'V': 0.0097,
     'W': 0.023, 'X': 0.001, 'Y': 0.019, 'Z': 0.0007}
mChunks = [cypherText[i:i + m] for i in range(0, len(cypherText), m)]
mChunks[-1] = mChunks[-1] + 'X' * (m - len(mChunks[-1]))
for i in range(m):
    chunk = ''.join([e[i] for e in mChunks])
    n = len(chunk)
    listCharFrequences = sorted(getCharFrequences(chunk).items(), key=itemgetter(0))
    indexList = [value[1] * (value[1] - 1) / (n * (n - 1)) for value in listCharFrequences]
    print 'Index c', i, sum(indexList)

key = ''
for k in range(m):
    chunk = ''.join([e[k] for e in mChunks])
    listCharFrequences = sorted(getCharFrequences(chunk).items(), key=itemgetter(0))
    maxG = ['A', 0, 0]
    for i in range(26):
        g = i
        mgList = [p[listCharFrequences[i][0]] * listCharFrequences[(i + g) % 26][1] / n for i in range(26)]
        if maxG[2] < sum(mgList):
            maxG[0] = listCharFrequences[g][0]
            maxG[1] = g
            maxG[2] = sum(mgList)
    print 'Mg ', maxG
    key += maxG[0]

print decrypt(key, cypherText)

