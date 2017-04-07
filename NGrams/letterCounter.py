from collections import Counter
import sys


def getCharFrequences(path):
    content = filter(str.isalpha, open(path).read()).lower()
    numEl = len(content)
    listChars = Counter(content).most_common()
    return [[c[0], c[1] / float(numEl)] for c in listChars]

if __name__ == '__main__':
    args = sys.argv
    f = getCharFrequences(args[1])
    for el in f:
        print el
