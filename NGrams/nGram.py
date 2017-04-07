from operator import itemgetter
from math import log
import matplotlib.pyplot as plt
import numpy as np
import sys


def getQGramsFrequences(n, path):
    content = filter(str.isalpha, open(
        path).read()).lower()
    nGram = {}
    bottom = 0
    for index in range(n, len(content) + 1):
        key = content[bottom:index]
        nGram[key] = nGram.get(key, 0) + 1
        bottom += 1
    lnGram = [(t[0], float(t[1])) for t in nGram.items()]
    return sorted(lnGram, key=itemgetter(1)), bottom

if __name__ == '__main__':
    args = sys.argv
    qValue = int(args[1])
    listQGramFrequences = getQGramsFrequences(qValue, args[3])
    qgrams = [e[0] for e in listQGramFrequences[0]]
    frequencies = [(e[1] / listQGramFrequences[1]) for e in listQGramFrequences[0]]
    pos = np.arange(len(qgrams))
    width = 1.0
    ax = plt.axes()
    if args[2] == 'a':
        for x in [(e[0], e[1] / listQGramFrequences[1]) for e in listQGramFrequences[0]]:
            print x
        plt.bar(pos, frequencies, width, color='#33cc33', edgecolor='black', tick_label=qgrams)
        plt.show()
    if args[2] == 'b':
        for x in [(e[0], e[1] / listQGramFrequences[1]) for e in listQGramFrequences[0]]:
            print x
        plt.bar(pos, frequencies, width, color='#33cc33')
        plt.show()
    if args[2] == 'c':
        indexList = [e[1] * (e[1] - 1) / (listQGramFrequences[1] * listQGramFrequences[1] - 1) for e in listQGramFrequences[0]]
        print 'Indice di coincidenza ', sum(indexList)
        entropia = [(e[1] / listQGramFrequences[1]) * log(e[1] / listQGramFrequences[1]) for e in listQGramFrequences[0]]
        print 'Entropia ', -sum(entropia) / log(listQGramFrequences[1])
