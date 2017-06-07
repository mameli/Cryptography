from heapq import heapify, heappush, heappop


def encode(probDistr):
    heap = [[(weight, -ord(symbol)), [symbol, ""]] for weight, symbol in probDistr]
    heapify(heap)
    print heap
    while len(heap) > 1:
        right = heappop(heap)
        left = heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [(left[0][0] + right[0][0], left[0][1] + right[0][1])] + left[1:] + right[1:])
        print heap
    codeList = heappop(heap)[1:]
    return sorted(codeList, key=lambda pair: (len(pair[1]), pair[0]))


probDistr = [(0.9, 'a'), (0.05, 'b'), (0.025, 'c'), (0.025, 'd')]
# probDistr = [(0.025, 'a'), (0.025, 'b'), (0.05, 'c'), (0.1, 'd'), (0.13, 'e'),(0.17, 'f'), (0.25, 'g'), (0.25, 'h')]
huffmanEncode = encode(probDistr)
print huffmanEncode
