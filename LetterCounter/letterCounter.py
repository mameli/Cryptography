from collections import Counter

def getCharFrequences():
    content = open('mobyDickAll.txt').read()
    content = filter(str.isalpha, content).lower()
    numEl = len(content)
    listChars = Counter(content).most_common()
    frequences = []
    for c in listChars:
        pair = (c[0], c[1] / float(numEl))
        frequences.append(pair)
    return frequences

if __name__ == '__main__':
    f = getCharFrequences()
    for el in f:
        print el
