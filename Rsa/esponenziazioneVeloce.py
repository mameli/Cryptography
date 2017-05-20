def expVeloce(a, n, m):
    d = 1
    binN = "{0:b}".format(n)
    for i in binN:
        d = (d * d) % m
        if i == '1':
            d = (d * a) % m
    return d