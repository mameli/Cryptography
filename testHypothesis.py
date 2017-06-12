import numpy as np
import string
import glob, os
from collections import Counter


ranDistribution = dict.fromkeys(string.ascii_lowercase, 1./26)
engDistribution = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228,
                   'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
                   'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987,
                   's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
                   'y': 0.01974, 'z': 0.00074}


def getCharFrequences(path):
    content = filter(str.isalpha, open(path).read()).lower()
    numEl = len(content)
    dictChars = dict.fromkeys(string.ascii_lowercase, 0)
    for c in Counter(content).most_common():
        dictChars[c[0]] = c[1] / float(numEl)
    return dictChars

def log2(p, q):
    if q == 0:
        return np.inf
    if p == 0:
        return 0
    return np.log2(p/q)

def kullbackLeiblerDivergence(p, q):
    return sum([p[c] * log2(p[c], q[c]) for c in p])


def shift(seq, n):
    return seq[n:] + seq[:n]


def hypothesisTest(text):
    frequences = getCharFrequences(text)
    engPQ = np.inf
    engQP = np.inf
    ranPQ = np.inf
    ranQP = np.inf
    tempDivengence = 0.
    for n in range(0, 26):
        shiftedFrequences = dict(zip(list(frequences.keys()), shift(list(frequences.values()), n)))
        tempDivengence = abs(kullbackLeiblerDivergence(engDistribution, shiftedFrequences))
        if engPQ > tempDivengence: 
            engPQ = tempDivengence
            engQP = abs(kullbackLeiblerDivergence(shiftedFrequences, engDistribution))
        tempDivengence = abs(kullbackLeiblerDivergence(ranDistribution, shiftedFrequences))
        if ranPQ > tempDivengence: 
            ranPQ = tempDivengence
            ranQP = abs(kullbackLeiblerDivergence(shiftedFrequences, ranDistribution))
    res = []
    res.append(text)
    if engPQ < ranPQ:
        res.append("eng")
        res.append(engPQ)
        res.append(pow(2, (-26 * engQP)))
        res.append(pow(2, (-26 * engPQ)))
    else:
        res.append("ran")
        res.append(ranPQ)
        res.append(pow(2, (-26 * ranQP)))
        res.append(pow(2, (-26 * ranPQ)))
    return res


if __name__ == '__main__':
    results = []
    os.chdir("text")
    for file in glob.glob("*.txt"):
        results.append(hypothesisTest(file))
    for r in results:
        print r
    engTextCounter = 0
    ranTextCounter = 0
    for r in results:
        if "eng" in r[1]:
            engTextCounter += 1
        if "ran" in r[1]:
            ranTextCounter += 1
    print "I testi in inglese sono ", engTextCounter
    print "I testi in random sono ", ranTextCounter
    # Test singolo
    print hypothesisTest("random44.txt")
